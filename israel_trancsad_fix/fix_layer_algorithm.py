import processing
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterFeatureSource,
)

from .transcad_crs import get_transcad_crs


class FixTranscadLayerAlgorithm(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(self.INPUT, "Input layer")
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT, "Output layer")
        )

    def processAlgorithm(self, parameters, context, feedback):
        # Step 1: reproject to EPSG:4326
        step1 = processing.run(
            "native:reprojectlayer",
            {
                "INPUT": parameters[self.INPUT],
                "TARGET_CRS": QgsCoordinateReferenceSystem("EPSG:4326"),
                "OUTPUT": "memory:",
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True,
        )

        # Step 2: reproject from EPSG:4326 to TransCAD Israel TM CRS
        step2 = processing.run(
            "native:reprojectlayer",
            {
                "INPUT": step1["OUTPUT"],
                "TARGET_CRS": get_transcad_crs(),
                "OUTPUT": "memory:",
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True,
        )

        # Step 3: assign EPSG:2039 CRS without reprojecting the coordinates
        step3 = processing.run(
            "native:assignprojection",
            {
                "INPUT": step2["OUTPUT"],
                "CRS": QgsCoordinateReferenceSystem("EPSG:2039"),
                "OUTPUT": parameters[self.OUTPUT],
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True,
        )

        return {self.OUTPUT: step3["OUTPUT"]}

    def name(self):
        return "fix_transcad_layer"

    def displayName(self):
        return "Fix TransCAD Layer"

    def shortHelpString(self):
        return (
            "Reprojects the input layer first to EPSG:4326, then to the "
            "TransCAD Israel TM CRS, and finally assigns EPSG:2039 as the "
            "declared CRS without further coordinate transformation."
        )

    def createInstance(self):
        return FixTranscadLayerAlgorithm()
