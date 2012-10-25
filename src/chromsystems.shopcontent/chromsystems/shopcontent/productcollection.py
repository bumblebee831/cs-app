from five import grok
from zope import schema
from plone.directives import dexterity, form

from plone.app.textfield import RichText
from plone.z3cform.textlines import TextLinesFieldWidget
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget

from chromsystems.shopcontent.orderableitem import IOrderableItem

from chromsystems.shopcontent import MessageFactory as _


class IProductCollection(form.Schema):
    """
    A collection of orderable products
    """
    #form.widget(relatedProducts=AutocompleteMultiFieldWidget)
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
    form.widget(headlines=TextLinesFieldWidget)
    headlines = schema.List(
        title=_(u"Headlines"),
        description=_(u"Headlines associated with this collection"),
        value_type=schema.TextLine(
            title=_(u"Headline"),
        ),
        required=False,
    )
    items = schema.TextLine(
        title=_(u"Orderable Items"),
        description=_(u"A list of headlines and related orderable items that "
                      u"stores the actual display order"),
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


class EditorView(grok.View):
    grok.context(IProductCollection)
    grok.require('cmf.ModifyPortalContent')
    grok.name('editor-view')
