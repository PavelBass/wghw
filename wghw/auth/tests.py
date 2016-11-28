from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from wghw.email_sender.models import User


class RegistrationViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username='regtest', email='regtest@test.com')
        cls.client = Client()
        super().setUpClass()

    def test_response_ok(self):
        respone = self.client.get(reverse('registration'))
        assert respone.status_code == 200

    def test_registration_post_ok(self):
        response = self.client.post(
            reverse('registration'),
            {'username': 'regtest1', 'password1': 'asdasd123', 'password2': 'asdasd123'},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 2)

    def test_registration_post_fail(self):
        response = self.client.post(
            reverse('registration'),
            {'username': 'regtest1', 'password1': 'asdasd123', 'password2': ''},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 0)
