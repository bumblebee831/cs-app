from Products.CMFCore.utils import getToolByName

def setupGroups(portal):
    acl_users = getToolByName(portal, 'acl_users')
    gtool = getToolByName(portal, 'portal_groups')
    if not acl_users.searchGroups(name='Worldwide'):
        gtool.addGroup('Worldwide', roles=['Member'])
    if not acl_users.searchGroups(name='GermanSpeakingCountries'):
        gtool.addGroup('GermanSpeakingCountries', roles=['Member'])
    if not acl_users.searchGroups(name='Netherlands'):
        gtool.addGroup('Netherlands', roles=['Member'])

def importVarious(context):
    """Miscellanous import steps handler"""
    if context.readDataFile('chromsystems.userdata-various.txt') is None:
        return
    
    portal = context.getSite()
    
    setupGroups(portal)
    