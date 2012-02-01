# -*- coding: utf-8 -*

from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish
from plone.app.contentlisting.interfaces import IContentListing

from kk.chproducts.interfaces import IProduct


class DuplicateContent(grok.View):
    grok.context(IContentish)
    grok.require('cmf.ManagePortal')
    grok.name('cleanup-duplicate-content')

    def update(self):
        self.has_products = len(self.products()) > 0
        self.request.set('disable_plone.rightcolumn',1)

    def products(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IProduct.__identifier__,
                          sort_on='sortable_title',
                          path=dict(query='/'.join(context.getPhysicalPath()),
                                    depth=5))
        products = IContentListing(results)
        return results

    def breadcrumbs(self, item):
        obj = item.getObject()
        view = getMultiAdapter((obj, self.request), name='breadcrumbs_view')
        # cut off the item itself
        breadcrumbs = list(view.breadcrumbs())[:-1]
        if len(breadcrumbs) == 0:
            # don't show breadcrumbs if we only have a single element
            return None
        if len(breadcrumbs) > 3:
            # if we have too long breadcrumbs, emit the middle elements
            empty = {'absolute_url': '', 'Title': unicode('…', 'utf-8')}
            breadcrumbs = [breadcrumbs[0], empty] + breadcrumbs[-2:]
        return breadcrumbs
