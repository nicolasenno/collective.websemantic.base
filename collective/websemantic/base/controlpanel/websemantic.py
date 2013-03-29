# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, \
    SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from collective.websemantic.base.interfaces import IRetriever
from plone.app.registry.browser import controlpanel
from zope.component import queryUtility
from zope.interface import Interface, implements
from zope import schema
from z3c.form.browser.select import SelectWidget
from z3c.form import group, field
from zope.schema import Field
from datatxt.client import FormDatatxtSettings
from zope.app.component.hooks import getSite 

class IWebSemanticSettings(Interface):
    """
    Web Semantic Base preference panel Interface
    """

    web_semantic_plugin = schema.Choice (
        title=u'Web semantic plugins names',
        description=_('help_web_semantic_plugins_names',
            default=u"Please select the Web semantic plugin."
        ),
        vocabulary=u"collective.websemantic.base.plugins_names",
        required=True,
    )


class SettingsGroup(group.Group):
    label = _(u"Settings")
    fields = field.Fields(IWebSemanticSettings)
    
    
def getGroups():
    portal=getSite()
    groups = [SettingsGroup,]
    retriever = queryUtility(IRetriever, 'plugins_setting_list_interfaces')
    if not retriever:
        return groups
    groups.extend(retriever(portal))
    return groups

class WebSemanticControlPanelEditForm(controlpanel.RegistryEditForm):

    label = _('Web Semantic Base settings')
    schema = IWebSemanticSettings
    groups = []
    description = _('Enter settings to use with this site.')
    form_name = _('Web Semantic Base')

    def update(self):
        """ Performe update in order to get all setting tabs
        """
        self.groups = getGroups()
        super(WebSemanticControlPanelEditForm, self).update()
        

class WebSemanticControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    Web Semantic Base preference panel form
    """

    form = WebSemanticControlPanelEditForm

