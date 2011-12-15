from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.chproducts.interfaces import ICSFolder
from kk.chproducts.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf

CSFolderSchema = folder.ATFolderSchema.copy() + document.ATDocumentSchema.copy()
class CSFolder(folder.ATFolder, document.ATDocument):
    """ folder with rich descrpition """
    
    implements(ICSFolder)
    portal_type=meta_type="CSFolder"
    schema = CSFolderSchema

registerType(CSFolder, PROJECTNAME)