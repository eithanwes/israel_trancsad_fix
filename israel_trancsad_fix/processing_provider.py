from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from .fix_layer_algorithm import FixTranscadLayerAlgorithm


class IsraelTranscadFixProvider(QgsProcessingProvider):
    """The provider of our plugin."""

    def loadAlgorithms(self):
        """Load each algorithm into the current provider."""
        self.addAlgorithm(FixTranscadLayerAlgorithm())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self) -> str:
        """The ID of your plugin, used for identifying the provider.

        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return "israel_trancsad_fix"

    def name(self) -> str:
        """The human friendly name of your plugin in Processing.

        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return self.tr("Israel Transcad Fix")

    def icon(self) -> QIcon:
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)
