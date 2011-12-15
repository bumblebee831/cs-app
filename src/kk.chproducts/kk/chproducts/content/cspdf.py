from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import file
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.chproducts.interfaces import ICSPDF
from kk.chproducts.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf
from Products.CMFCore.utils import getToolByName

CSPDFSchema = file.ATFileSchema.copy() + Schema((
    StringField('organiser',
              searchable=True,
              widget = StringWidget(
                        label = 'Organiser',
                        label_msgid = 'label_organiser',
					),
    ),  
    BooleanField('inst_manual',
              searchable=True,
              widget = BooleanWidget(
                        label = 'Instruction manual',
                        label_msgid = 'label_inst_manual',
					),
    ), 
    BooleanField('safety_data_sheet',
              searchable=True,
              widget = BooleanWidget(
                        label = 'Safety Data Sheet',
                        label_msgid = 'label_safety_data_sheet',
					),
    ), 
    LinesField('parameter',
              searchable=True,
              multiValued = True,
              addable = True,
              widget = KeywordWidget(
                        label = 'Parameters',
                        label_msgid = 'label_parameters',
					),
    ),          
))

class CSPDF(file.ATFile):
    """ file with extra fields """
    
    implements(ICSPDF)
    portal_type=meta_type="CSPDF"
    schema = CSPDFSchema

    def getParametersString(self):
        parameters = self.getParameter()
        return ", ".join(parameters)
        
    def getParametersIndex(self):
        ptool = getToolByName(self, 'portal_catalog')
        return ptool.uniqueValuesFor('parameters')   
    def SearchableText(self):
        text =self.Title()+" "+ " ".join(self.Title().split("_")) + " "+ self.getParametersString() + " "+self.Description() + " "+ self.getOrganiser()
        return text
registerType(CSPDF, PROJECTNAME)