from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from collective.websemantic.base.interfaces import IWebSemanticPlugin
from zope.component import getGlobalSiteManager
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def pluginsNames(context):
    """ Vocabulary factory for web semantic plugins
    """
    sm = getGlobalSiteManager()
    plugins = [SimpleTerm("", "", _("-- select a plugin --"))]
    import pdb;pdb.set_trace()
    for adapter in sm.registeredAdapters():
        if adapter.provided == IWebSemanticPlugin:
            plugins.append(SimpleTerm(value="",
                                      token="",
                                      title=_("-- select a plugin --")))

    return SimpleVocabulary(plugins)

