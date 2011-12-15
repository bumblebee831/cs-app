from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class CSFolderView(BrowserView):
    """ cs plain folder view """
    __call__ = ViewPageTemplateFile('templates/plain_list.pt')
    
    def SearchResults(self, q, search):
        if search == "0":
            return []
        query = {}
        query['path'] = "/".join(self.context.getPhysicalPath())
        query['portal_type'] = "CSPDF"
        if self.request.get('sort_on'):
            sort_on = self.request.get('sort_on')
        else:
            sort_on = "sortable_title" 
            
        if self.request.get('sort_dest'):
            sort_dest = self.request.get('sort_dest')
        else:
            sort_dest = "ascending"         
        query['sort_on'] = sort_on
        query['sort_order'] = sort_dest
        
        if q:
            query['SearchableText'] = q
        results = self.context.portal_catalog(**query);
        return results
        
class CSFolderTabularView(CSFolderView):
    """ cs tabular folder view """
    __call__ = ViewPageTemplateFile('templates/tabular_list.pt')
    
    def getSortDest(self, dest):
        if dest == "ascending":
            return "descending"
        else:
            return "ascending"
