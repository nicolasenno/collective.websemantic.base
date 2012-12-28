from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
WebsemanticBaseMessageFactory = MessageFactory(u'collective.websemantic.base')

class Layer(Interface):
    """Layer Marker"""

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
