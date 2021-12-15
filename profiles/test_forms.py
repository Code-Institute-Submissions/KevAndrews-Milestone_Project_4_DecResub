"""
Test Class for the Profile Forms
"""
from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    """
    Class for Testing the Profile Form
    """

    def test_phone_number_in_form(self):
        """
        Test if the Phone Number field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_phone_number', form.fields)

    def test_street_address_1_in_form(self):
        """
        Test if the Street Address 1 field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_street_address1', form.fields)

    def test_street_address_2_in_form(self):
        """
        Test if the Street Address 2 field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_street_address2', form.fields)

    def test_town_or_city_in_form(self):
        """
        Test if the Town or City field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_town_or_city', form.fields)

    def test_county_in_form(self):
        """
        Test if the County field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_county', form.fields)

    def test_postcode_in_form(self):
        """
        Test if the Postcode field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_postcode', form.fields)

    def test_country_in_form(self):
        """
        Test if the Country field is in the form
        """
        form = UserProfileForm()
        self.assertIn('default_country', form.fields)

    def test_user_in_form(self):
        """
        Test if the Country field is in the form
        """
        form = UserProfileForm()
        self.assertNotIn('user', form.fields)

    def test_fields_are_not_in_form_metaclass(self):
        """
        Test if the explictied fields in the Meta class are working
        """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
