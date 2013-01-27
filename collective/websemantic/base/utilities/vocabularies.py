from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from websemantic.base.interfaces import IWebSemanticPlugin
from zope.component import getGlobalSiteManager
from zope.interfaces import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class Plugins(object):
    """ Vocabulary factory for web semantic plugins
    """
    implements(IVocabularyFactory)
    
    def call(self):
        """ Returns a SimpleVocabulary of available web semantic plugins
        """
        sm = getGlobalSiteManager()
        plugins = [SimpleTerm("","",_("-- select a plugin --"))]
        for adapter in sm.registeredAdapters():
            if adapter.provided == IWebSemanticPlugin:
                plugins.append(SimpleTerm(value="",
                                          token="",
                                          title = _("-- select a plugin --")))
        
        return SimpleVocabulary(plugins)
        
        