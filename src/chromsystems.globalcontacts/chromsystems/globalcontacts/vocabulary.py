from five import grok
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from chromsystems.globalcontacts import MessageFactory as _


class VitaminProfilingVocabulary(object):
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        TYPES = {   _(u"Vitamins B1/B6"): 'vitamins-b1-b6',
                    _(u"Vitamin B1"): 'vitamins-b1',
                    _(u"Vitamin B2"): 'vitamins-b2',
                    _(u"Vitamin B6"): 'vitamins-b3',
                    _(u"Vitamins A/E"): 'vitamins-a-e',
                }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value
                                in TYPES.iteritems()
                                ])
grok.global_utility(VitaminProfilingVocabulary,
                    name=u"chromsystems.globalcontacts.VitaminProfiling")
