from five import grok
from plone.directives import dexterity, form

from zope import schema
from plone.namedfile.interfaces import IImageScaleTraversable

from chromsystems.shopcontent import MessageFactory as _


# Interface class; used to define content-type schema.

class IOrderableItem(form.Schema, IImageScaleTraversable):
    """
    A single orderable item
    """
    productCode = schema.TextLine(
        title=_(u"Product Code"),
        required=True,
    )


class OrderableItem(dexterity.Item):
    grok.implements(IOrderableItem)


class View(grok.View):
    grok.context(IOrderableItem)
    grok.require('zope2.View')
    grok.name('view')
