from qgis.core import QgsCoordinateReferenceSystem

# User-defined CRS based on TransCAD Israel TM projection (GRS80 ellipsoid, Transverse Mercator)
TRANSCAD_CRS_WKT = """PROJCRS["unknown",
    BASEGEOGCRS["unknown",
        DATUM["D_Unknown_based_on_GRS80_ellipsoid",
            ELLIPSOID["GRS 1980",6378137,298.257222101,
                LENGTHUNIT["metre",1],
                ID["EPSG",7019]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["Degree",0.0174532925199433]]],
    CONVERSION["unnamed",
        METHOD["Transverse Mercator",
            ID["EPSG",9807]],
        PARAMETER["Latitude of natural origin",31.7343936111111,
            ANGLEUNIT["Degree",0.0174532925199433],
            ID["EPSG",8801]],
        PARAMETER["Longitude of natural origin",35.2045169444444,
            ANGLEUNIT["Degree",0.0174532925199433],
            ID["EPSG",8802]],
        PARAMETER["Scale factor at natural origin",1.0000067,
            SCALEUNIT["unity",1],
            ID["EPSG",8805]],
        PARAMETER["False easting",219529.584,
            LENGTHUNIT["metre",1],
            ID["EPSG",8806]],
        PARAMETER["False northing",626907.39,
            LENGTHUNIT["metre",1],
            ID["EPSG",8807]]],
    CS[Cartesian,2],
        AXIS["(E)",east,
            ORDER[1],
            LENGTHUNIT["metre",1,
                ID["EPSG",9001]]],
        AXIS["(N)",north,
            ORDER[2],
            LENGTHUNIT["metre",1,
                ID["EPSG",9001]]]]"""


TRANSCAD_CRS_NAME = "TransCAD Israel TM (GRS80)"


def get_transcad_crs() -> QgsCoordinateReferenceSystem:
    """Return a QgsCoordinateReferenceSystem built from the TransCAD WKT definition."""
    crs = QgsCoordinateReferenceSystem()
    crs.createFromWkt(TRANSCAD_CRS_WKT)
    return crs


