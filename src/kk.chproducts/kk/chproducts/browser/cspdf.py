from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class CSPDFView(BrowserView):
    """ cs folder view """
    __call__ = ViewPageTemplateFile('templates/cspdf.pt')