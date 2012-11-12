from five import grok
from plone.directives import dexterity, form

from chromsystems.shopcontent import MessageFactory as _


class IItemRepository(form.Schema):
    """
    A repository for products including management dashboard
    """


class ItemRepository(dexterity.Container):
    grok.implements(IItemRepository)


class View(grok.View):
    grok.context(IItemRepository)
    grok.require('zope2.View')
    grok.name('view')
