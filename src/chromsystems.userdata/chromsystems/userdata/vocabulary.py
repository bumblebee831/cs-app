from five import grok
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.i18n.locales.interfaces import ICountryAvailability

from chromsystems.userdata import _


class CountryListVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        utility = queryUtility(ICountryAvailability)
        countrycodes = utility.getCountryListing()
        countrylist = {}
        for code in countrycodes:
            countrylist[code[0]] = code[1]
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                 for value, title in
                                 sorted(countrylist.iteritems())])

grok.global_utility(CountryListVocabulary,
                    name=u"chromsystems.userdata.CountryList")
