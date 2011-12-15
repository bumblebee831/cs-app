from zope.interface import implements
from zope.component import adapts
from AccessControl import ClassSecurityInfo 
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import document, image
from Products.ATContentTypes.content.base import ATCTFileContent
from Products.ATContentTypes.content.document import ATDocumentBase
from Products.ATContentTypes.content.image import ATCTImageTransform

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.chproducts.interfaces import IProduct
from kk.chproducts.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf
from plone.app.blob.field import  ImageField as BlobImageField
from Products.CMFCore.permissions import View
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName


ProductSchema = folder.ATFolderSchema.copy()  + Schema((
    ReferenceField('categories', 
    				required=True, 
     			    allowed_types=('ProductCategory'), 
    			    multiValued = True, 
    			    vocabulary = "getCategoriesValues", 
    			    relationship="product_categories",  				
    				widget=ReferenceWidget(label="Categories")), 
    

    TextField('text',
              required=False,
              searchable=True,
              primary=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              #validators = ('isTidyHtml',),
              default_output_type = 'text/x-html-safe',
              widget = RichWidget(
                        description = '',
                        label = 'label_body_text',
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),  
        
    BooleanField('tableContents',
        required = False,
        languageIndependent = True,
        widget = BooleanWidget(
            label= 'help_enable_table_of_contents',
            description = "help_enable_table_of_contents_description"
            )
    ),                                                  
                                                             
))
ProductSchema["subject"].schemata = "default"
ProductSchema["subject"].required = True
ProductSchema["tableContents"].widget.visible = {"edit": "invisible", "view": "invisible"}
class Product(ATCTImageTransform, folder.ATFolder, document.ATDocument):
    """ product """
    schema = ProductSchema
    implements(IProduct)
    portal_type=meta_type="Product"
    security = ClassSecurityInfo()
    
    security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.Title()
        return self.getField('image').tag(self, **kwargs)
    
    
    def getCategoriesValues(self):
        ptool = getToolByName(self, "portal_catalog")
        cats = [ (i.UID, i.Title) for i in ptool(portal_type="ProductCategory") ]
        return DisplayList(tuple(cats))
        
    def getCategoriesIndex(self):
        return [i.UID() for i in self.getCategories()]  
        
    def getCategoriesList(self):
        return ", ".join(["<a href='%s'>%s</a>" % (i.absolute_url(), i.Title()) for i in self.getCategories()])
        
registerType(Product, PROJECTNAME)
