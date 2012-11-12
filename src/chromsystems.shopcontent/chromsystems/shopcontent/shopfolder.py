from five import grok
from plone.directives import dexterity, form


class IShopFolder(form.Schema):
    """
    A folderish type acting as shop dashboard
    """


class ShopFolder(dexterity.Container):
    grok.implements(IShopFolder)


class View(grok.View):
    grok.context(IShopFolder)
    grok.require('zope2.View')
    grok.name('view')
