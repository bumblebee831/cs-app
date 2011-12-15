from plone.app.portlets.portlets.login import Renderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Acquisition import aq_base, aq_inner

class MyRenderer(Renderer):
    render = ViewPageTemplateFile('login.pt')
    def show(self):
        #if not self.portal_state.anonymous():
        #    return False
        if not self.pas_info.hasLoginPasswordExtractor():
            return False
        page = self.request.get('URL', '').split('/')[-1]
        return page not in ('login_form', '@@register')


    @property
    def available(self):
        return self.show()
    def is_auth(self):
        return not self.portal_state.anonymous()   
    @memoize
    def user_name(self):
        context = aq_inner(self.context)
        member = self.portal_state.member()
        userid = member.getId()
        membership = getToolByName(context, 'portal_membership')
        member_info = membership.getMemberInfo(member.getId())
        if member_info:
            fullname = member_info.get('fullname', '')
        else:
            fullname = None
        if fullname:
            user_name = fullname
        else:
            user_name = userid
        return user_name



    