from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    def get_salutation(self):
        return unicode(self.context.getProperty('salutation', ''), 'utf-8')

    def set_salutation(self, value):
        return self.context.setMemberProperties({'salutation': value})
    salutation = property(get_salutation, set_salutation)

    def get_firstname(self):
        return unicode(self.context.getProperty('firstname', ''), 'utf-8')

    def set_firstname(self, value):
        return self.context.setMemberProperties({'firstname': value})
    firstname = property(get_firstname, set_firstname)

    def get_lastname(self):
        return unicode(self.context.getProperty('lastname', ''), 'utf-8')

    def set_lastname(self, value):
        return self.context.setMemberProperties({'lastname': value})
    lastname = property(get_lastname, set_lastname)

    def get_customer(self):
        return unicode(self.context.getProperty('customer', ''), 'utf-8')

    def set_customer(self, value):
        return self.context.setMemberProperties({'customer': value})
    customer = property(get_customer, set_customer)

    def get_company(self):
        return unicode(self.context.getProperty('company', ''), 'utf-8')

    def set_company(self, value):
        return self.context.setMemberProperties({'company': value})
    company = property(get_company, set_company)

    def get_street(self):
        return unicode(self.context.getProperty('street', ''), 'utf-8')

    def set_street(self, value):
        return self.context.setMemberProperties({'street': value})
    street = property(get_street, set_street)

    def get_city(self):
        return unicode(self.context.getProperty('city', ''), 'utf-8')

    def set_city(self, value):
        return self.context.setMemberProperties({'city': value})
    city = property(get_city, set_city)

    def get_zipcode(self):
        return unicode(self.context.getProperty('zipcode', ''), 'utf-8')

    def set_zipcode(self, value):
        return self.context.setMemberProperties({'zipcode': value})
    zipcode = property(get_zipcode, set_zipcode)

    def get_country(self):
        return unicode(self.context.getProperty('country', ''), 'utf-8')

    def set_country(self, value):
        return self.context.setMemberProperties({'country': value})
    country = property(get_country, set_country)

    def get_phone(self):
        return unicode(self.context.getProperty('phone', ''), 'utf-8')

    def set_phone(self, value):
        return self.context.setMemberProperties({'phone': value})
    phone = property(get_phone, set_phone)

    def get_fax(self):
        return unicode(self.context.getProperty('fax', ''), 'utf-8')

    def set_fax(self, value):
        return self.context.setMemberProperties({'fax': value})
    fax = property(get_fax, set_fax)

    def get_comment(self):
        return unicode(self.context.getProperty('comment', ''), 'utf-8')

    def set_comment(self, value):
        return self.context.setMemberProperties({'comment': value})
    comment = property(get_comment, set_comment)
