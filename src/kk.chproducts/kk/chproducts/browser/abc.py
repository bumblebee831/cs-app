# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from kk.chproducts.config import ABC_GROUPPED 
from Products.CMFPlone.utils import safe_unicode
class ABCView(BrowserView):
    """ abc view """
    __call__ = ViewPageTemplateFile('templates/abc_view.pt')
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.keywords = list(self.context.portal_catalog.uniqueValuesFor('Subject'))
 
    def abc(self):
        return ABC_GROUPPED    		  
    def searchKeywords(self, group_num = "0"):
        group_num = int(group_num)
    	chars = ABC_GROUPPED[group_num]  	
        chars_uni = chars[1]
    	return [k for k in self.keywords if unicode(k, "utf-8")[0].upper() in chars_uni ]
  
    

    