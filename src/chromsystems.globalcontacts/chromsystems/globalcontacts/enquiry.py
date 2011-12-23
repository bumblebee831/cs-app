from five import grok
from plone.directives import form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder

from zope.component import getMultiAdapter
from zope.component import queryUtility
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import getVocabularyRegistry
from z3c.form import group, field, button
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioWidget

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.interfaces import IContentish
from plone.registry.interfaces import IRegistry

from chromsystems.globalcontacts import MessageFactory as _


class RegistrySource(object):
    grok.implements(IContextSourceBinder)

    def __init__(self, key):
        self.key = key

    def __call__(self, context):
        registry = queryUtility(IRegistry)
        terms = []
        if registry is not None:
            for value in registry.get(self.key, ()):
                terms.append(
                    SimpleVocabulary.createTerm(
                        value, value.encode('utf-8'), value))
        return SimpleVocabulary(terms)


class IEnquiry(form.Schema):
    """ Enquiry form schema composed of several interfaces as a
        group form.
    """
    salutation = schema.Choice(
        title=_(u"Salutation"),
        values = [
            _(u'Mrs.'),
            _(u'Mr.'), ],
        default=u'Mrs.',
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
        required=False,
    )
    email = schema.TextLine(
        title=_(u'Email'),
        required=True,
    )
    requested_material = schema.FrozenSet(
        title=_(u"Requested Material"),
        value_type=schema.Choice(
            vocabulary=u"chromsystems.globalcontacts.AvailableMaterial",
        ),
        required=True,
    )
    message = schema.Text(
        title=_(u"Your Message"),
        required=False,
    )
    newborn_screening = schema.FrozenSet(
        title=_(u"Newborn Screening"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.newbornScreening'),
        ),
        required=False,
    )
    drug_monitoring = schema.FrozenSet(
        title=_(u"Therapeutic Drug Monitoring"),
        description=_(u"MassTox(R) TDM Series A-Parameter Sets, "
                      u"LC-MS/MS Analysis"),
        value_type=schema.Choice(
        source=RegistrySource(
            'chromsystems.globalcontacts.therapeuticDrugMonitoring'),
        ),
        required=False,
    )
    alcohol_abuse = schema.Set(
        title=_(u"Bio-markers for alcohol abuse"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.alcoholAbuseMarkers'),
        ),
        required=False,
    )
    oxidative_stress_monitoring = schema.FrozenSet(
        title=_(u"Monitoring Oxidative Stress"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.monitoringOxidativeStress'),
        ),
        required=False,
    )
    vitamin_profiling = schema.FrozenSet(
        title=_(u"Vitamin Profiling"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.alcoholAbuseMarkers'),
        ),
        required=False,
    )
    arteriosclerosis = schema.FrozenSet(
        title=_(u"Risk Factors for Arteriosclerosis"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.arteriosclerosisRiskFactors'),
        ),
        required=False,
    )
    porphyrins_diagnosis = schema.FrozenSet(
        title=_(u"Diagnosis for Porphyrins"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.porphyrinsDiagnosis'),
        ),
        required=False,
    )
    osteoporosis_diagnosis = schema.FrozenSet(
        title=_(u"Osteoporosis Diagnosis"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.osteoporosisDiagnosis'),
        ),
        required=False,
    )
    hemoglobin_testing = schema.FrozenSet(
        title=_(u"Hemoglobin Testing"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.hemoglobinTesting'),
        ),
        required=False,
    )
    biogenic_amines = schema.FrozenSet(
        title=_(u"Biogenic Amines (Phaeochromocytoma)"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.biogenicAmines'),
        ),
        required=False,
    )
    controls = schema.FrozenSet(
        title=_(u"Controls"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.controls'),
        ),
        required=False,
    )
    calibration = schema.FrozenSet(
        title=_(u"Calibration"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.calibration'),
        ),
        required=False,
    )
    occupational_medicine = schema.FrozenSet(
        title=_(u"Occupational Medicine"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.occupationalMedicine'),
        ),
        required=False,
    )
    hplc = schema.FrozenSet(
        title=_(u"HPLC Instruments and Software"),
        value_type=schema.Choice(
            source=RegistrySource(
            'chromsystems.globalcontacts.instrumentsAndSoftware'),
        ),
        required=False,
    )


class ContactGroup(group.Group):
    label=u"Contact Details"
    description=u"Enter your contact details below"
    fields=field.Fields(IEnquiry).select(
        'salutation', 'firstname', 'lastname', 'institution', 'street',
        'postalcode', 'city', 'country', 'phone', 'fax', 'email',
        )
#fields['salutation'].widgetFactory = RadioWidget

class PreferencesGroup(group.Group):
    label=u"Enter Preferences"
    description=u"Enter your preferences below"
    fields=field.Fields(IEnquiry).select(
        'requested_material', 'message',
        )
    fields['requested_material'].widgetFactory = CheckBoxFieldWidget


class InterestsGroup(group.Group):
    label=u"Area of Interest"
    description=u"Please select your area of interest"
    fields=field.Fields(IEnquiry).select(
        'newborn_screening', 'drug_monitoring', 'alcohol_abuse',
        'oxidative_stress_monitoring', 'vitamin_profiling',
        'arteriosclerosis', 'porphyrins_diagnosis', 'osteoporosis_diagnosis',
        'hemoglobin_testing', 'biogenic_amines', 'controls', 'calibration',
        'occupational_medicine', 'hplc',
        )
    fields['newborn_screening'].widgetFactory = CheckBoxFieldWidget
    fields['drug_monitoring'].widgetFactory = CheckBoxFieldWidget
    fields['alcohol_abuse'].widgetFactory = CheckBoxFieldWidget
    fields['oxidative_stress_monitoring'].widgetFactory = CheckBoxFieldWidget
    fields['vitamin_profiling'].widgetFactory = CheckBoxFieldWidget
    fields['arteriosclerosis'].widgetFactory = CheckBoxFieldWidget
    fields['porphyrins_diagnosis'].widgetFactory = CheckBoxFieldWidget
    fields['osteoporosis_diagnosis'].widgetFactory = CheckBoxFieldWidget
    fields['hemoglobin_testing'].widgetFactory = CheckBoxFieldWidget
    fields['biogenic_amines'].widgetFactory = CheckBoxFieldWidget
    fields['controls'].widgetFactory = CheckBoxFieldWidget
    fields['calibration'].widgetFactory = CheckBoxFieldWidget
    fields['occupational_medicine'].widgetFactory = CheckBoxFieldWidget
    fields['hplc'].widgetFactory = CheckBoxFieldWidget


class EnquiryForm(group.GroupForm, form.Form):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('enquiry')

    schema = IEnquiry
    ignoreContext = True
    ignoreRequest = False
    css_class = 'overlayForm'

    label = _(u"Contact")
    description = _(u"Please fill out the form to send an enquiry.")

    groups = (ContactGroup, PreferencesGroup, InterestsGroup)
    enable_form_tabbing = False

    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)
        super(EnquiryForm, self).update()

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
        contactinfo = self.context.contact.to_object
        mailto = contactinfo.email
        bcc = contactinfo.additional_email
        if bcc:
            mto = (u"%s, %s") % (mailto, bcc)
        else:
            mto = mailto
        envelope_from = data['email']
        subject = _(u'Anfrage von %s %s') % (
            data['firstname'], data['lastname'])
        options = data
        options['recipientname'] = contactinfo.Title()
        options['url'] = context_url
        body = ViewPageTemplateFile("enquiry_email.pt")(self, **options)
        # send email
        mailhost = getToolByName(self.context, 'MailHost')
        mailhost.send(body, mto=mto, mfrom=envelope_from, subject=subject,
                      charset='utf-8')
        IStatusMessage(self.request).addStatusMessage(
            _(u"Your email has been forwarded."),
            type="info")
        return self.request.response.redirect(context_url+'/@@thank-you')

    def contact_info(self):
        context = aq_inner(self.context)
        related_contact = context.contact.to_object
        if related_contact:
            #result = results[0]
            obj = related_contact
            info = dict(
                title=obj.Title(),
                salutation=obj.salutation,
                email=obj.email,
                phone=obj.phone,
                imageTag=self.constructImageTag(obj),
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
