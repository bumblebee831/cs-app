# -*- coding: utf-8 -*

from Acquisition import aq_inner
from Acquisition import aq_parent
from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from kk.chproducts.config import ABC_GROUPPED


class SearchForm(BrowserView):
    """ search form """
    __call__ = ViewPageTemplateFile('templates/search_form.pt')

    def getKeywords(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        keywords = []
        keywords.append("")
        return keywords + list(catalog.uniqueValuesFor('Subject'))

    def getKeywordsString(self):
        q = self.request.get("q", "")
        keywords = list(self.context.portal_catalog.uniqueValuesFor('Subject'))
        return "\n".join(["%s|%s" % (k, k) for k in keywords
                          if k.decode("utf-8").lower().startswith(
                                                    q.decode("utf-8"))])

    def getABC(self):
        return ABC_GROUPPED


class SearchResultsView(BrowserView):
    """ search results """

    template = ViewPageTemplateFile('templates/search_results.pt')

    def __call__(self):
        return self.template()

    def KeywordQuery(self):
        keyword = self.request.get("keyword", "")
        mode = self.request.get("mode", "0")
        if mode == "0":
            return [k for k in keyword.split(",")
                    if k.decode("utf-8").lower().strip() != ""]
        else:
            return [keyword, ]

    def Keywords(self):
        keyword = self.request.get("keyword", "")
        mode = self.request.get("mode", "0")
        if mode == "0":
            k_list = []
            for k in keyword.split(","):
                st = k.decode("utf-8").strip()
                if st:
                    st1 = st[0].lower()+st[1:]
                    st2 = st[0].upper()+st[1:]
                    k_list.append(st1.encode('utf-8'))
                    k_list.append(st2.encode('utf-8'))
            return k_list
        else:
            return [keyword, ]

    def doSearch(self):
        keyword = self.Keywords()
        category = self.getActiveCategory()
        query = {}
        query['portal_type'] = 'Product'
        if keyword:
            query['Subject'] = keyword
        query['sort_on'] = 'sortable_title'
        if category:
            query['product_categories'] = category
        products = self.context.portal_catalog(**query)
        return products

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

    def getActiveCategory(self):
        categories = self.getCategories()
        for cat in categories:
            if cat['is_active']:
                return cat['category'].UID
        return None

    def getCategories(self):
        cat_uid = self.request.get("category", "")
        categories = self.context.portal_catalog(
                        portal_type="ProductCategory",
                        sort_on="getObjPositionInParent")
        result = []
        if cat_uid:
            i = 0
            for cat in categories:
                is_active = False
                if cat_uid == cat.UID:
                    is_active = True
                result.append({"category": cat, "is_active": is_active})
                i = i+1
        return result
