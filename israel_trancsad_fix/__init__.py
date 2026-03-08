from .israel_trancsad_fix_plugin import IsraelTranscadFixPlugin


def classFactory(iface):
    return IsraelTranscadFixPlugin(iface)
