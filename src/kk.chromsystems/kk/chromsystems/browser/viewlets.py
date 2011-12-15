from cgi import escape
from zope.component import getMultiAdapter
from zope.interface import implements

from Acquisition import aq_inner, aq_parent

from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.navtree import buildFolderTree

from Products.CMFPlone import utils
from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder
 
from plone.app.portlets.portlets.navigation import Assignment
from plone.app.layout.viewlets import common
from plone.app.layout.viewlets import content

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from kk.chromsystems.interfaces import IStaticEnabled

class StaticViewlet(common.ViewletBase):
    render = ViewPageTemplateFile('templates/kk_static.pt')

    def is_portal_root(self):
        context = aq_inner(self.context)
        request = aq_inner(self.request)
        context_state = getMultiAdapter((context, request), name=u'plone_context_state')
        is_portal_root = context_state.is_portal_root()
        return is_portal_root
    
    def is_static_enabled(self):
        context = aq_inner(self.context)
        if IStaticEnabled.providedBy(context):
            return True
        else:
            return False  

from kk.chromsystems.interfaces import IStaticGCEnabled 

class StaticGCViewlet(common.ViewletBase):
    render = ViewPageTemplateFile('templates/kk_static_gc.pt')

    def is_portal_root(self):
        context = aq_inner(self.context)
        request = aq_inner(self.request)
        context_state = getMultiAdapter((context, request), name=u'plone_context_state')
        is_portal_root = context_state.is_portal_root()
        return is_portal_root

    def is_static_gc_enabled(self):
        context = aq_inner(self.context)
        if IStaticGCEnabled.providedBy(context):
            return True
        else:
            return False
