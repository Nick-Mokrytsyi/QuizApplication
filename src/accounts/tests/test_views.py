from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.signing import Signer
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from ..models import User


class TestViews(TestCase):
    def setUp(self):
        self.data = {
            'username': 'user_1',
            'password1': '123qwe!@#',
            'password2': '123qwe!@#',
            'email': 'user_1@test.com',
        }
        self.client = Client()
        self.registration_url = reverse('accounts:register')
        self.registration_done_url = reverse('accounts:register_done')
        self.user_reactivate_url = reverse('accounts:update_activation')

    def test_page_not_found(self):
        response = self.client.get('/non-existing-page')
        self.assertEqual(response.status_code, 404)

    def test_reactivate_form_displayed_on_get_request(self):
        response = self.client.get(reverse('accounts:update_activation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/user_reactivate.html')
        self.assertIn('form', response.context)

    def test_invalid_form_data(self):
        data = {'email': 'invalid-email'}
        response = self.client.post(self.user_reactivate_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/user_reactivate.html')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.has_error('email'))

    def test_email_not_found(self):
        data = {'email': 'non-existing@test.com'}
        response = self.client.post(self.user_reactivate_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/no_user_in_database.html')

    def test_user_already_activated(self):
        self.user = get_user_model().objects.create_user(
            username='username',
            email='test@emal.com',
            password='testpassword',
            is_active=True,
            is_activated=True,
        )
        data = {'email': self.user.email}
        response = self.client.post(self.user_reactivate_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/user_is_activated.html')

    @patch('accounts.views.send_activation_notification')
    def test_activation_notification(self, mock_send_activation_notification):
        self.user = get_user_model().objects.create_user(
            username='username_test',
            email='test@example.com',
            password='new@emailtest.com',
            is_active=False,
            is_activated=False,
        )
        data = {'email': self.user.email}
        response = self.client.post(self.user_reactivate_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/user_register_done.html')
        mock_send_activation_notification.assert_called_once_with(self.user)

    def test_registration_valid(self):
        response = self.client.post(self.registration_url, self.data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.registration_done_url, status_code=302, target_status_code=200)
        self.assertEqual(response.url, self.registration_done_url)

        user = User.objects.first()
        self.assertEqual(user.username, self.data['username'])
        self.assertEqual(user.email, self.data['email'])
        self.assertTrue(user.check_password(self.data['password1']))
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_activated)

    def test_registration_invalid(self):
        self.data['password2'] = '123qwe!@'

        response = self.client.post(self.registration_url, self.data)
        self.assertNotEqual(response.status_code, 302)
        self.assertFalse(response.context['form'].is_valid())
        user = User.objects.filter(username=self.data['username'])
        self.assertEqual(len(user), 0)

    def test_activation_url(self):
        response = self.client.post(self.registration_url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.registration_done_url, status_code=302, target_status_code=200)

        user = User.objects.first()
        self.assertEqual(user.username, self.data['username'])

        signer = Signer()
        response = self.client.get(
            'http://localhost' + reverse('accounts:register_activate', kwargs={'sign': signer.sign(user.username)})
        )
        self.assertEqual(response.status_code, 200)

        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_activated)
