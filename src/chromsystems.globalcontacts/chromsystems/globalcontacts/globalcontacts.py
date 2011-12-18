from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema

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
            scale = scales.scale('image', scale='thumb')
            imageTag = None
            if scale is not None:
                imageTag = scale.tag()
            import pdb; pdb.set_trace( )
            results.append({
                    'url': contact.absolute_url(),
                    'title': contact.title,
                    'summary': contact.description,
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
