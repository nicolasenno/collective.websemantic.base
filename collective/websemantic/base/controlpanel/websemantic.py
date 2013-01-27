# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, \
    SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.registry.browser import controlpanel
from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from zope.component import adapts
from zope.interface import Interface, implements
from zope.schema import Choice, Text


class IWebSemanticSettings(Interface):
    """
    Web Semantic Base preference panel Interface
    """
    
    web_semantic_plugin = Choice (
        title=u'Web semantic plugin',
        description=_('help_web_semantic_plugin',
            default=u"Please select the Web semantic plugin."
        ),
        required=True,
        vocabulary = "websemantic.base.plugins",
    )


class WebSemanticControlPanelEditForm(controlpanel.RegistryEditForm):

    schema = IWebSemanticSettings
    label = _('Web Semantic Base settings')
    description = _('Enter settings to use with this site.')
    form_name = _('Web Semantic Base')

    def updateFields(self):
        super(WebSemanticControlPanelEditForm, self).updateFields()

    def updateWidgets(self):
        super(WebSemanticControlPanelEditForm, self).updateWidgets()


class WebSemanticControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    Web Semantic Base preference panel form
    """
    form = WebSemanticControlPanelEditForm

