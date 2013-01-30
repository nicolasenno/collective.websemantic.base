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

    web_semantic_plugins = Choice (
        title=u'Web semantic plugins names',
        description=_('help_web_semantic_plugins_names',
            default=u"Please select the Web semantic plugin."
        ),
        vocabulary=u"plugins_names",
        required=True,
    )


class WebSemanticControlPanelEditForm(controlpanel.RegistryEditForm):

    label = _('Web Semantic Base settings')
    schema = IWebSemanticSettings
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

