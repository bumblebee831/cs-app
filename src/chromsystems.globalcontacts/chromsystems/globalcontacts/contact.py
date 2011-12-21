from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema

from plone.indexer import indexer
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from chromsystems.globalcontacts import MessageFactory as _


# Interface class; used to define content-type schema.

class IContact(form.Schema, IImageScaleTraversable):
    """
    A contact person.
    """
    title = schema.TextLine(
        title=_(u"Contact Name"),
        description=_(u"Enter a title for this contact."),
        required=True,
    )
    salutation = schema.Choice(
        title=_(u"label_salutation"),
        values = [_(u"Frau"), _(u"Herr"), ],
        default=u"Frau",
        required=True,
    )
    phone = schema.TextLine(
        title=_(u"Phone"),
        required=True,
    )
    email = schema.TextLine(
        title=_(u"Email"),
        description=_(u"Enter email address used in enquiry forms."),
        required=True,
    )
    additional_email = schema.TextLine(
        title=_(u"BCC Email Adresses"),
        description=_(u"Enter optional additional email addresses "
                      u"seperated by commas."),
        required=False,
    )
    image = NamedBlobImage(
        title=_(u"Portrait Image"),
        description=_(u"Upload a portrait of the contact person."),
        required=True,
    )


@indexer(IContact)
def contactCountriesIndexer(obj):
    if obj.countries is None:
        return None
    return obj.countries
grok.global_adapter(contactCountriesIndexer, name="countries")


class Contact(dexterity.Item):
    grok.implements(IContact)


class View(grok.View):
    grok.context(IContact)
    grok.require('zope2.View')
    grok.name('view')
