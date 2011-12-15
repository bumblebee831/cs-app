from plone.app.layout.viewlets.common import SearchBoxViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
class KKSearchBoxViewlet (SearchBoxViewlet):
    render = ViewPageTemplateFile("templates/kk_searchbox.pt")