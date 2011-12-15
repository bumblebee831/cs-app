from plone.app.users.browser.register import RegistrationForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser import RadioWidget as _RadioWidget
from chromsystems.userdata import _


class CustomRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form to provide
        custom widgets for our custom form fields.
    """
    label = _(u'heading_registration_form', default=u'Registration form')
    description = _(u"Please fill in the registration form details.")
    template = ViewPageTemplateFile('register_form.pt')

    @property
    def form_fields(self):
        fields = super(CustomRegistrationForm, self).form_fields
        fields['salutation'].custom_widget = CustomRadioWidget
        return fields


def CustomRadioWidget(field, request):
    """Widget for salutation field.
    """
    vocabulary = field.vocabulary
    widget = _RadioWidget(field, vocabulary, request)
    return widget
