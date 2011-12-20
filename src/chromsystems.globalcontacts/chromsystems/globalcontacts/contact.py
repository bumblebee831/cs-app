from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.vocabulary import getVocabularyRegistry

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.indexer import indexer
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
    #form.widget(countries=AutocompleteMultiFieldWidget)
    countries = schema.Set(
        title=_(u"Country"),
        description=_(u"Please select the countries this contact is "
                      u"responsible for"),
        value_type = schema.Choice(
            vocabulary=u"chromsystems.userdata.CountryList",
        )
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

    def prettyprinted_countries(self):
        context = aq_inner(self.context)
        vr = getVocabularyRegistry()
        countries_vocabulary = vr.get(context,
            'chromsystems.userdata.CountryList')
        countries = context.countries
        if countries:
            countrylist = []
            for country in countries:
                countryinfo = {}
                term = countries_vocabulary.getTerm(country)
                countryinfo['title'] = term.title
                countryinfo['value'] = term.value
                countrylist.append(countryinfo)
            return countrylist
