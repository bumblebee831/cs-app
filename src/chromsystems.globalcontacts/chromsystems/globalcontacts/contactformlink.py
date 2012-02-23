from Acquisition import aq_inner
from AccessControl import getSecurityManager
from five import grok
from plone.memoize.instance import memoize
from plone.directives import dexterity, form
from zope import schema

from z3c.form import group, field

from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.autocomplete import AutocompleteFieldWidget

from chromsystems.globalcontacts.contact import IContact
from chromsystems.globalcontacts import MessageFactory as _


# Interface class; used to define content-type schema.

class IContactFormLink(form.Schema):
    """
    A basic content type holding a reference to related contacts.
    """
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"This is most probably a country name."),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        description=_(u"Optional textual description for this item."),
        required=False,
    )

    form.widget(contact=AutocompleteFieldWidget)
    contact = RelationChoice(
        title=_(u"Responsible Contact"),
        source=ObjPathSourceBinder(object_provides=IContact.__identifier__),
        required=True,
    )
    headline = schema.TextLine(
        title=_(u"Headline"),
        description=_(u"Enter headline for the author information. "
                      u"The country will be appended automatically."),
        required=False,
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


class ContactFormLink(dexterity.Item):
    grok.implements(IContactFormLink)


class View(grok.View):
    grok.context(IContactFormLink)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        if not self.can_edit:
            self.request.response.redirect(self.form_url())
        else:
            self.request.response.redirect(self.form_url())

    @memoize
    def can_edit(self):
        return bool(getSecurityManager().checkPermission(
                    'Review portal content',
                    self.context))

    def form_url(self):
        context = aq_inner(self.context)
        context_url = context.absolute_url()
        form_url = context_url + '/@@enquiry'
        return form_url

class ThankYou(grok.View):
    grok.context(IContactFormLink)
    grok.require('zope2.View')
    grok.name('thank-you')

    def update(self):
        context = aq_inner(self.context)
        self.contact = context.contact
        if self.contact:
            contact_obj = self.contact.to_object
            self.thank_you = contact_obj.thank_you.output
