from five import grok
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from chromsystems.globalcontacts import MessageFactory as _


class AvailableMaterialVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        TYPES = {_(u"Data Sheet"): 'Data Sheet',
                 _(u"Instruction Manual"): 'Instruction Manual',
                 _(u"Price/Delivery Information"):
                    'Price/Delivery Information',
                }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value in TYPES.iteritems()])
grok.global_utility(AvailableMaterialVocabulary,
                    name=u"chromsystems.globalcontacts.AvailableMaterial")
