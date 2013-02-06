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
            import pdb;pdb.set_trace()
            factory = adapter.factory(self)
            property = factory.settingsClassForm
            if property:
                settings_classes.append(property)
    return settings_classes



#class Retriever(object):
#    """ todo
#    """
#
#    def interfacensDottedNames(self):
#        """ Returns a list of dotted interface name from all
#            websemantic plugins
#        """
#        settings_classes = []
#        sm = getGlobalSiteManager()
#        for adapter in sm.registeredAdapters():
#            if adapter.provided == IWebSemanticPlugin:
#                import pdb;pdb.set_trace()
#                factory = adapter.factory(self)
#                property = factory.settingsClassForm
#                if property:
#                    settings_classes.append(property)
#
#        return settings_classes
#RetrieverFactory = Retriever()


