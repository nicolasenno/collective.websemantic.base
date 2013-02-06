from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from collective.websemantic.base.interfaces import IWebSemanticPlugin
from collective.websemantic.base.interfaces import IRetriever
from zope.component import getGlobalSiteManager
from zope.interface import implements

class Retriever(object):

    implements(IRetriever)

    def interfacensDottedNames(self, context):
        """ Returns a list of dotted interface name from all
            websemantic plugins
        """
        dotted_names = []
        sm = getGlobalSiteManager()
        for adapter in sm.registeredAdapters():
            if adapter.provided == IWebSemanticPlugin:
                factory = adapter.factory
                property = factory.settings_interface
                if property:
                    dotted_names.append(property.fget(adapter.factory))

        return dotted_names

