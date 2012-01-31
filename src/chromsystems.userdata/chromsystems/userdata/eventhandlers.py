from five import grok
from zope.site.hooks import getSite
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.events import (
    IPrincipalCreatedEvent)
from Products.PlonePAS.interfaces.events import IUserInitialLoginInEvent

MESSAGE_TEMPLATE = """\
A new user %(user)s has requested membership for %(title)s.

No Action is required on your part. You will be notified upon the users's
initial login to the site.
"""
LOGIN_MESSAGE = """\
The user %(user)s has logged in for the first time.

You may want to visit
%(editlink)s
to review the user details and configure group membership.

"""


@grok.subscribe(IPrincipalCreatedEvent)
def notifyOnMemberCreation(event):
    portal = getSite()
    mto = 'service@chromsystems.de'
    envelope_from = 'service@chromsystems.de'
    subject = 'New user has registered to chromsystems.de'
    info = {}
    info['user'] = event.principal
    info['title'] = portal.Title()
    message = MESSAGE_TEMPLATE % info
    # send email
    mailhost = getToolByName(portal, 'MailHost')
    mailhost.send(message, mto=mto, mfrom=envelope_from,
                  subject=subject, charset='utf-8')


@grok.subscribe(Interface, IUserInitialLoginInEvent)
def notifyNewUserLoggedIn(principal, event):
    portal = getSite()
    portal_url = portal.absolute_url()
    info = {}
    user = event.principal
    username = user.getId()
    editlink = '/@@usergroup-userprefs?searchstring=%s' % username
    info['user'] = username
    info['editlink'] = portal_url + editlink 
    mto = 'service@chromsystems.de'
    envelope_from = 'service@chromsystems.de'
    subject = 'New member %s has authenticated' % username
    message = LOGIN_MESSAGE % info
    mailhost = getToolByName(portal, 'MailHost')
    mailhost.send(message, mto=mto, mfrom=envelope_from,
                  subject=subject, charset='utf-8')
