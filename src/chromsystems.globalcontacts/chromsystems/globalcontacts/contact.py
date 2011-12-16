from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget

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
    image = NamedBlobFile(
        title=_(u"Portrait Image"),
        description=_(u"Upload a portrait of the contact person."),
        required=True,
    )
    form.widget(countries=AutocompleteMultiFieldWidget)
    countries = schema.Set(
        title=_(u"Country"),
        description=_(u"Please select the countries this contact is "
                      u"responsible for"),
        value_type = schema.Choice(
            vocabulary=u"chromsystems.userdata.CountryList",
        )
    )


class Contact(dexterity.Item):
    grok.implements(IContact)


class View(grok.View):
    grok.context(IContact)
    grok.require('zope2.View')
    grok.name('view')
