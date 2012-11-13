from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form
from Products.CMFCore.utils import getToolByName

from plone.app.contentlisting.interfaces import IContentListing

from chromsystems.shopcontent.itemcollection import IItemCollection


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


class DashboardCollections(grok.View):
    grok.context(IShopFolder)
    grok.require('cmf.ModifyPortalContent')
    grok.name('dashboard-collections')

    def update(self):
        self.has_collections = len(self.item_collections()) > 0

    def item_collections(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog(object_provides=IItemCollection.__identifier__,
                         path=dict(query='/'.join(context.getPhysicalPath()),
                                   depth=1),
                         sort_on='modified',
                         sort_order='reverse',
                         review_state='published')
        results = IContentListing(brains)
        return results
