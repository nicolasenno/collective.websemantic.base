from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, \
    SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from datatxt.client import WebsemanticBaseMessageFactory as _
from plone.app.registry.browser import controlpanel
from zope.component import adapts
from zope.interface import Interface, implements
from zope.schema import TextLine


class IDatatxtSettings(Interface):
    """
    Datatxt Preference Panel Interface
    """
    app_key = TextLine (
        title=u'Datatxt app key',
        description=_('help_datatxt_app_key',
            default=u"Please enter your application key"
        ),
        required=True,
        default=u'',
    )
    app_id = TextLine (
        title=u'Datatxt app id',
        description=_('help_datatxt_app_id',
            default=u"Please enter your application id"
        ),
        required=True,
        default=u'',
    )
    app_lang = TextLine (
        title=u'Datatxt language',
        description=_('help_datattx_lang',
            default=u'Please enter language for the enancher'
        ),
        required=True,
        default=u'it',
    )
    api_url = TextLine (
        title=u'Datatxt url',
        description=_('help_datatxt_url',
            default=u'Please enter Datatxt url'
        ),
        required=True,
        default=u'http://spaziodati.eu/datatxt/v3/',
    )
    rho = TextLine (
        title=u'Datatxt rho',
        description=_('help_datatxt_rho',
            default=u'Please enter rho number'
        ),
        required=True,
        default=u'0.1',
    )
    epsilon = TextLine (
        title=u'Datatxt epsilon',
        description=_('help_datatxt_epsilon',
            default=u'Please enter epsilon'
        ),
        required=True,
        default=u'0.3',
    )
    long_text = TextLine (
        title=u'Datatxt long text',
        description=_('help_datatxt_long_text',
            default=u'Please enter lenght'
        ),
        required=True,
        default=u'0',
    )
    dbpedia = TextLine (
        title=u'Datatxt server port',
        description=_('help_dbpedia_url',
            default=u'Please enter DBpedia url'
        ),
        required=True,
        default=u'http://it.dbpedia.org',
    )


class DatatxtControlPanelEditForm(controlpanel.RegistryEditForm):

    schema = IDatatxtSettings
    label = _('Datatxt server settings')
    description = _('Enter Datatxt server settings to use with this site.')
    form_name = _('Datatxt')

    def updateFields(self):
        super(DatatxtControlPanelEditForm, self).updateFields()

    def updateWidgets(self):
        super(DatatxtControlPanelEditForm, self).updateWidgets()


class DatatxtControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    Datatxt Control Panel Form
    """
    form = DatatxtControlPanelEditForm

