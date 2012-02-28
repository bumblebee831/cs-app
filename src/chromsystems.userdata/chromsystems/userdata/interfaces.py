from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IChromsystemsUserdata(IDefaultPloneLayer):
    """ A marker interface for the package layer
    """


class IAdminNotification(Interface):
    """ A utility capable of notifying a site administrator
    of newly created principals
    """

    def __call__(info):
        """ Notify Site Administrator """
