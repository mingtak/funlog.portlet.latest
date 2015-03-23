from zope.i18nmessageid import MessageFactory
LastestPublishMessageFactory = MessageFactory('funlog.portlet.latest')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
