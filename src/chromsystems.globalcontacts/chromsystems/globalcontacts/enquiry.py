from five import grok
from plone.directives import form

from zope import schema
from zope.component import getMultiAdapter
from zope.schema.vocabulary import getVocabularyRegistry
from z3c.form import button

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.interfaces import IContentish

from chromsystems.globalcontacts.contact import IContact
from chromsystems.globalcontacts import MessageFactory as _


class IEnquiry(form.Schema):
    """ Enquiry form schema composed of several interfaces as a
        group form.
    """
    salutation = schema.Choice(
        title=_(u"Salutation"),
        values = [
            _(u'Frau'),
            _(u'Herr'), ],
        default=u'Frau',
        required=True,
    )
    firstname = schema.TextLine(
        title=_(u"First name"),
        required=True,
    )
    lastname = schema.TextLine(
        title=_(u"Last name"),
        required=True,
    )
    institution = schema.TextLine(
        title=_(u"Institution"),
        required=False,
    )
    street = schema.TextLine(
        title=_(u"Street"),
        required=True,
    )
    postalcode = schema.TextLine(
        title=_(u"Postal Code"),
        required=True,
    )
    city = schema.TextLine(
        title=_(u"City"),
        required=True,
    )
    country = schema.TextLine(
        title=_(u"Country"),
        required=True,
    )
    phone = schema.TextLine(
        title=_(u"Phone"),
        required=True,
    )
    fax = schema.TextLine(
        title=_(u"Fax"),
        required=True,
    )
    email = schema.TextLine(
        title=_(u'Email'),
        required=True,
    )
    message = schema.Text(
        title=_(u"Message"),
        required=False,
    )


class EnquiryForm(form.SchemaForm):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('enquiry')

    schema = IEnquiry
    ignoreContext = True
    css_class = 'overlayForm'

    label = _(u"Contact")
    description = _(u"Please fill out the form to send an enquiry.")

    def updateActions(self):
        super(EnquiryForm, self).updateActions()
        self.actions["submit"].addClass("btn cta large")
        self.actions['cancel'].addClass("btn large")

    @button.buttonAndHandler(_(u'Send now'), name='submit')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.status = self.send_email(data)

    @button.buttonAndHandler(_(u'cancel'))
    def handleCancel(self, action):
        context = aq_inner(self.context)
        context_url = context.absolute_url()
        return self.request.response.redirect(context_url)

    def send_email(self, data):
        """ Construct and send an enquiry email. """
        context_url = self.context.absolute_url()
        mto = self.context.email
        envelope_from = data['email']
        subject = _(u'Anfrage von %s') % data['name']
        options = dict(email = data['email'],
                       name = data['name'],
                       message = data['message'],
                       url = context_url,
                        )
        body = ViewPageTemplateFile("enquiry_email.pt")(self, **options)
        # send email
        mailhost = getToolByName(self.context, 'MailHost')
        mailhost.send(body, mto=mto, mfrom=envelope_from, subject=subject, charset='utf-8')

        IStatusMessage(self.request).addStatusMessage(
            _(u"Your email has been forwarded.", "info")
            )

        return self.request.response.redirect(context_url)
    
    def contact_info(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        self.contact = self.request.get('contact', '')
        if self.contact:
            results = catalog(object_provides=IContact.__identifier__,
                              review_state='published',
                              countries=self.contact)
            if results:
                result = results[0]
                obj = result.getObject()
                info = dict(
                    title=obj.Title(),
                    salutation=obj.salutation,
                    email=obj.email,
                    phone=obj.phone,
                    imageTag=self.constructImageTag(obj),
                    country=self.prettyprint_country(self.contact),
                )
                return info

    def constructImageTag(self, obj):
        scales = getMultiAdapter((obj, self.request), name='images')
        scale = scales.scale('image', scale='thumb')
        imageTag = None
        if scale is not None:
            imageTag = scale.tag()
        return imageTag

    def prettyprint_country(self, country):
        context = aq_inner(self.context)
        vr = getVocabularyRegistry()
        countries_vocabulary = vr.get(context,
            'chromsystems.userdata.CountryList')
        term = countries_vocabulary.getTerm(country)
        return term.title
        