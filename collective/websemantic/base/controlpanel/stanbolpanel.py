from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, \
    SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from collective.websemantic.base import WebsemanticBaseMessageFactory as _
from plone.app.registry.browser import controlpanel
from zope.component import adapts
from zope.interface import Interface, implements
from zope.schema import Int, TextLine, Tuple, Text


class IStanbolSettings(Interface):
    """
    Stanbol Preference Panel Interface
    """
    stanbol_server_protocol = TextLine (
        title=u'Stanbol server protocol',
        description=_('help_stanbol_server_protocol',
            default=u"Please enter the protocol of your Stanbol server instance"
        ),
        required=True,
        default=u'http',
    )
    stanbol_server_host = TextLine (
        title=u'Stanbol server host',
        description=_('help_stanbol_server_host',
            default=u"Please enter the host of your Stanbol server instance"
        ),
        required=True,
        default=u'localhost',
    )
    stanbol_server_port = TextLine (
        title=u'Stanbol server port',
        description=_('help_stanbol_server_port',
            default=u'Please enter the port of your Stanbol server instance'
        ),
        required=True,
        default=u'9000',
    )

class StanbolControlPanelEditForm(controlpanel.RegistryEditForm):

    schema = IStanbolSettings
    label = _('Stanbol server settings')
    description = _('Enter Stanbol server settings to use with this site.')
    form_name = _('Stanbol')

    def updateFields(self):
        super(StanbolControlPanelEditForm, self).updateFields()


    def updateWidgets(self):
        super(StanbolControlPanelEditForm, self).updateWidgets()


class StanbolControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    Stanbol Control Panel Form
    """
    form = StanbolControlPanelEditForm

