from five import grok
from plone.directives import dexterity, form

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from chromsystems.shopcontent.orderableitem import IOrderableItem

from chromsystems.shopcontent import MessageFactory as _


class IProductCollection(form.Schema):
    """
    A collection of orderable products
    """
    relatedProducts = RelationList(
        title=_(u"Related Products"),
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            source=ObjPathSourceBinder(
                object_provides=IOrderableItem.__identifier__)
        ),
        required=False,
    )
    text = RichText(
        title=_(u"Descriptive Text"),
        description=_(u"Optional additional information on this selection"),
        required=False,
    )


class ProductCollection(dexterity.Item):
    grok.implements(IProductCollection)


class View(grok.View):
    grok.context(IProductCollection)
    grok.require('zope2.View')
    grok.name('view')
