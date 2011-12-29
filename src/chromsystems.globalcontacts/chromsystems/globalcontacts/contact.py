from five import grok
from plone.directives import dexterity, form

from zope import schema

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText

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
        values = [_(u"Mrs"), _(u"Mr"), ],
        default=u"Mrs",
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
    text = RichText(
        title=_(u"Textual Information"),
        description=_(u"Enter optional contact information that will be used "
                      u"in the contact view instead of the auto generated "
                      u"information based on single fields."),
        required=False,
    )
    thank_you = RichText(
        title=_(u"Thank-you Page Text"),
        description=_(u"Please enter the specific thank-you text for this "
                      u"contact that will be displayed on form submission."),
        required=True,
    )


class Contact(dexterity.Item):
    grok.implements(IContact)


class View(grok.View):
    grok.context(IContact)
    grok.require('zope2.View')
    grok.name('view')
