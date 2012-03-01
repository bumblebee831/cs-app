# -*- coding: utf-8 -*

from five import grok
from zope.site.hooks import getSite
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.PlonePAS.interfaces.events import IUserInitialLoginInEvent


LOGIN_MESSAGE = """\
The user %(user)s has logged in for the first time.
------------
Name: %(firstname)s %(lastname)s
Customer ID: %(customer)s
Company: %(company)s
Address: %(zipcode)s %(city)s, %(street)s
Country: %(country)s
Phone: %(phone)s
Fax: %(fax)s
------------

Comment:
%(comment)s

You may want to visit
%(editlink)s
to review the user details and configure group membership.

"""


@grok.subscribe(Interface, IUserInitialLoginInEvent)
def notifyNewUserLoggedIn(principal, event):
    portal = getSite()
    portal_url = portal.absolute_url()
    info = {}
    user = event.principal
    username = user.getId()
    mtool = getToolByName(portal, 'portal_membership')
    member = mtool.getMemberById(username)
    editlink = '/@@usergroup-userprefs?searchstring=%s' % username
    info['user'] = username
    info['editlink'] = portal_url + editlink
    info['firstname'] = safe_unicode(member.getProperty('firstname', ''))
    info['lastname'] = safe_unicode(member.getProperty('lastname', ''))
    info['customer'] = safe_unicode(member.getProperty('customer', ''))
    info['company'] = safe_unicode(member.getProperty('company', ''))
    info['street'] = safe_unicode(member.getProperty('street', ''))
    info['zipcode'] = safe_unicode(member.getProperty('zipcode', ''))
    info['city'] = safe_unicode(member.getProperty('city', ''))
    info['country'] = safe_unicode(member.getProperty('country', ''))
    info['phone'] = safe_unicode(member.getProperty('phone', ''))
    info['fax'] = safe_unicode(member.getProperty('fax', ''))
    info['comment'] = safe_unicode(member.getProperty('comment', ''))
    mto = 'service@chromsystems.de'
    envelope_from = 'service@chromsystems.de'
    subject = 'New member %s has authenticated' % username
    message = LOGIN_MESSAGE % info
    mailhost = getToolByName(portal, 'MailHost')
    mailhost.send(message, mto=mto, mfrom=envelope_from,
                  subject=subject, charset='utf-8')
