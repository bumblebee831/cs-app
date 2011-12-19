from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.vocabulary import getVocabularyRegistry

from z3c.form import group, field
from zope.component import getMultiAdapter

from plone.namedfile.interfaces import IImageScaleTraversable
from Products.CMFCore.utils import getToolByName
from plone.app.contentlisting.interfaces import IContentListing

from chromsystems.globalcontacts.contact import IContact
from chromsystems.globalcontacts import MessageFactory as _


# Interface class; used to define content-type schema.

class IGlobalContacts(form.Schema, IImageScaleTraversable):
    """
    A collection of contact persons.
    """


class GlobalContacts(dexterity.Container):
    grok.implements(IGlobalContacts)


class View(grok.View):
    grok.context(IGlobalContacts)
    grok.require('zope2.View')
    grok.name('view')
    
    def update(self):
        self.has_contacts = len(self.contained_contacts()) > 0

    def contacts(self):
        contacts = self.contained_contacts()
        results = []
        for contact in contacts:
            obj = contact.getObject()
            scales = getMultiAdapter((obj, self.request), name='images')
            scale = scales.scale('image', scale='tile')
            imageTag = None
            if scale is not None:
                imageTag = scale.tag()
            results.append({
                    'url': obj.absolute_url(),
                    'title': obj.Title(),
                    'salutation': obj.salutation,
                    'countries': self.countries_vocab(obj.countries),
                    'phone': obj.phone,
                    'email': obj.email,
                    'imageTag': imageTag,
                })
        return results

    def contained_contacts(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IContact.__identifier__,
                          path='/'.join(context.getPhysicalPath()),
                          review_state='published',)
        contacts = IContentListing(results)
        return results

    def countries_vocab(self, countries):
        context = aq_inner(self.context)
        vr = getVocabularyRegistry()
        countries_vocabulary = vr.get(context,
            'chromsystems.userdata.CountryList')
        countrylist = []
        for country in countries:
            countryinfo = {}
            term = countries_vocabulary.getTerm(country)
            countryinfo['title'] = term.title
            countryinfo['value'] = term.value
            countrylist.append(countryinfo)
        return countrylist
