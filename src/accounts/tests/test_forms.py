from django.test import TestCase

from ..forms import UserRegisterForm


class TestForms(TestCase):

    def setUp(self):
        self.username = 'user_1'
        self.password = '123qwe!@#'
        self.email = 'user_1@test.com'

    def test_register_form_valid_data(self):
        form = UserRegisterForm(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password
            }
        )

        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
