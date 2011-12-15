from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.chproducts.interfaces import IProductCategory
from kk.chproducts.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf

class ProductCategory(folder.ATFolder):
    """ category folder """
    
    implements(IProductCategory)
    portal_type=meta_type="ProductCategory"
    

registerType(ProductCategory, PROJECTNAME)