from five import grok
from zope.site.hooks import getSite
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from Products.PlonePAS.interfaces.events import IUserInitialLoginInEvent


LOGIN_MESSAGE = """\
The user %(user)s has logged in for the first time.
------------
Name: %(fullname)s
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
    info['fullname'] = member.getProperty('fullname', '')
    info['customer'] = member.getProperty('customer', '')
    info['company'] = member.getProperty('company', '')
    info['street'] = member.getProperty('street', '')
    info['zipcode'] = member.getProperty('zipcode', '')
    info['city'] = member.getProperty('city', '')
    info['country'] = member.getProperty('country', '')
    info['phone'] = member.getProperty('phone', '')
    info['fax'] = member.getProperty('fax', '')
    info['comment'] = member.getProperty('comment', '')
    mto = 'service@chromsystems.de'
    envelope_from = 'service@chromsystems.de'
    subject = 'New member %s has authenticated' % username
    message = LOGIN_MESSAGE % info
    mailhost = getToolByName(portal, 'MailHost')
    mailhost.send(message, mto=mto, mfrom=envelope_from,
                  subject=subject, charset='utf-8')
