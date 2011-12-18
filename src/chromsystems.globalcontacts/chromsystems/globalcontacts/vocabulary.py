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


class NewbornScreeningVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        TYPES = {
        _(u'MassChrom Amino Acids and Acylcarnitines, LC-MS/MS Analysis'):
            'MassChrom Amino Acids and Acylcarnitines, LC-MS/MS Analysis',
        _(u'MassChrom Amino Acids and Acylcarnitines/Non Derivatised, '
          u'LC-MS/MS Analysis'):
        'MassChrom Amino Acids and Acylcarnitines/Non Derivatised,'
        'LC-MS/MS Analysis',
        }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value in TYPES.iteritems()])
grok.global_utility(NewbornScreeningVocabulary,
                    name=u"chromsystems.globalcontacts.NewbornScreening")


class DrugMonitoringVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        TYPES = {
        _(u'Amiodarone/Desethylamiodarone'):
           'Amiodarone/Desethylamiodarone',
        _(u'Antidepressants 1, MassTox LC-MS/MS Analysis'):
           'Antidepressants 1, MassTox LC-MS/MS Analysis',
        _(u'Antidepressants 2/Psychostimulants, MassTox LC-MS/MS Analysis'):
           'Antidepressants 2/Psychostimulants, MassTox LC-MS/MS Analysis',
        _(u'Anti-HIV Drugs'):
           'Anti-HIV Drugs',
        _(u'Antiepileptic Drugs'):
           'Antiepileptic Drugs',
        _(u'Benzodiazepines, Tricyclic Antidepressants'):
           'Benzodiazepines, Tricyclic Antidepressants',
        _(u'Imatinib, Dasatinib, Nilotinib'):
           'Imatinib, Dasatinib, Nilotinib',
        _(u'Immunosuppressants, MassTox LC-MS/MS Analysis'):
           'Immunosuppressants, MassTox LC-MS/MS Analysis',
        _(u'Itraconazole, Posaconazole, Voriconazole'):
           'Itraconazole, Posaconazole, Voriconazole',
        _(u'Levetiracetam (Keppra)'):
           'Levetiracetam (Keppra)',
        _(u'Mycophenolic Acid'):
           'Mycophenolic Acid',
        _(u'Mycophenolic Acid, MassTox LC-MS/MS Analysis'):
           'Mycophenolic Acid, MassTox LC-MS/MS Analysis',
        _(u'Neuroleptics 1, MassTox LC-MS/MS Analysis'):
           'Neuroleptics 1, MassTox LC-MS/MS Analysis',
        _(u'Neuroleptics 2, MassTox LC-MS/MS Analysis'):
           'Neuroleptics 2, MassTox LC-MS/MS Analysis',
        _(u'Olanzapine/Desmethylolanzapine'):
           'Olanzapine/Desmethylolanzapine',
        _(u'Rufinamide, Felbamate, Lacosamide'):
           'Rufinamide, Felbamate, Lacosamide',
            }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value in TYPES.iteritems()])
grok.global_utility(DrugMonitoringVocabulary,
                    name=u"chromsystems.globalcontacts.DrugMonitoring")


class VitaminProfilingVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        TYPES = {_(u"Vitamins B1/B6"): 'Vitamins B1/B6',
                 _(u"Vitamin B1"): 'Vitamin B1',
                 _(u"Vitamin B2"): 'Vitamin B2',
                 _(u"Vitamin B6"): 'Vitamin B6',
                 _(u"Vitamins A/E"): 'Vitamins A/E',
                }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value in TYPES.iteritems()])
grok.global_utility(VitaminProfilingVocabulary,
                    name=u"chromsystems.globalcontacts.VitaminProfiling")
