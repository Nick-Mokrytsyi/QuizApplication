from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.views.generic import TemplateView

from src.accounts.views import (
    UserRegisterView, UserLoginView, UserLogoutView, user_profile_view,
    UserProfileUpdateView, user_activate, user_reactivate
)


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)

    def test_register_activate_url_resolves(self):
        url = reverse('accounts:register_activate', kwargs={'sign': 'notmetterwhatullwritehere'})
        self.assertEqual(resolve(url).func, user_activate)

    def test_register_done_url_resolves(self):
        url = reverse('accounts:register_done')
        self.assertEqual(resolve(url).func.view_class, TemplateView)

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, user_profile_view)

    def test_profile_update_url_resolves(self):
        url = reverse('accounts:profile_update')
        self.assertEqual(resolve(url).func.view_class, UserProfileUpdateView)

    def test_update_activation_url_resolves(self):
        url = reverse('accounts:update_activation')
        self.assertEqual(resolve(url).func, user_reactivate)
