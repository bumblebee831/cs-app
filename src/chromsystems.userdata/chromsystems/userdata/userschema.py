from zope.interface import Interface, implements
from zope import schema
#from plone.directives import form
from z3c.form.browser.radio import RadioWidget
from chromsystems.userdata import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    salutation = schema.Choice(
        title=_(u'label_salutation', default=u'Salutation'),
        values = [
            _(u'Frau'),
            _(u'Herr'), ],
        default=u'Frau',
        required=True,
        )
    firstname = schema.TextLine(
        title=_(u'label_firstname', default=u'First name'),
        required=False,
        )
    lastname = schema.TextLine(
        title=_(u'label_lastname', default=u'Last name'),
        required=False,
        )
    customer = schema.TextLine(
        title=_(u'label_customer', default=u'Customer'),
        description=_(u'help_customer',
            default=u'Please enter your customer identification.'),
        required=False,
        )
    company = schema.TextLine(
        title=_(u'label_company', default=u'Company'),
        required=False,
        )
    street = schema.TextLine(
        title=_(u'label_street', default=u'Street'),
        required=False,
        )
    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        required=False,
        )
    zipcode = schema.TextLine(
        title=_(u'label_zipcode', default=u'Zipcode'),
        )
    country = schema.Choice(
        title=_(u'label_country', default=u'Country'),
        vocabulary=u"chromsystems.userdata.CountryList",
        required=False,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        required=False,
        )
    fax = schema.TextLine(
        title=_(u'label_fax', default=u'Fax number'),
        required=False,
        )
    comment = schema.Text(
        title=_(u'label_comments', default=u'Comments'),
        description=_(u'help_comments',
                      default=u"If you have any comments concerning your "
                        "registration, please leave them here."),
        required=False,
        )
