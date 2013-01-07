from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from logging import getLogger

WebsemanticBaseMessageFactory = MessageFactory(u'collective.websemantic.base')

logger = getLogger('collective.websemantic.base')

class Layer(Interface):
    """Layer Marker"""

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
