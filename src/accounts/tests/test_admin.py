from django.test import TestCase

from ..models import User
from ..admin import UserAdmin


class TestAdminAvatarImage(TestCase):

    def setUp(self):
        self.username = 'user_1'
        self.password = '123qwe!@#'
        self.email = 'user_1@test.com'
        self.avatar = 'test_avatar.jpg'

    def test_avatar_img(self):
        user = User.objects.create(username=self.username, email=self.email, avatar=self.avatar)
        admin = UserAdmin(User, None)
        avatar_html = admin.avatar_img(user)
        expected_html = f'<img src="{user.avatar.url}" alt="{user.username}" width="50" height="50">'
        self.assertEqual(str(avatar_html), expected_html)
