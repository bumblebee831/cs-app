from Acquisition import aq_inner
from five import grok

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish


class CleanupWordwideGroup(grok.View):
    grok.context(IContentish)
    grok.require('cmf.ManagePortal')
    grok.name('cleanup-wordwide-group')

    def update(self):
        context = aq_inner(self.context)
        acl_users = getToolByName(context, 'acl_users')
        portal_groups = getToolByName(context, 'portal_groups')
        users = context.acl_users.getUsers()
        for user in users:
            portal_groups.addPrincipalToGroup(user.getUserName(), 'Worldwide')

    def render(self):
        return 'Updated worldwide group to contain all user records'
