from zope.interface import Interface

class IProductCategory(Interface):
    """ category for product """
    
class IProduct(Interface):
    """ product """

class ICSFolder(Interface):
    """ folder with rich description """

class ICSPDF(Interface):
    """ pdf with extra fields """