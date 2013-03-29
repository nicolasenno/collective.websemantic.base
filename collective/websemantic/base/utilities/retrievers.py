from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from collective.websemantic.base.interfaces import IWebSemanticPlugin
from collective.websemantic.base.interfaces import IRetriever
from zope.component import getGlobalSiteManager
from zope.interface import implements


def getSettingsClasses(self):
    """ Returns a list of dotted interface name from all
    websemantic plugins
    """

    settings_classes = []
    sm = getGlobalSiteManager()
    for adapter in sm.registeredAdapters():
        if adapter.provided == IWebSemanticPlugin:
            factory = adapter.factory()
            property = factory.settingsClassForm
            if property:
                settings_classes.append(property)
    return tuple(settings_classes)




