from urllib.parse import urlparse

from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from wghw.email_sender.models import Message, User


class EmailSendModelsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create(username='esmodeltest', email='esmodeltest@test.com')
        cls.message = Message.objects.create(
            user=user,
            email_to='a@a.com',
            text='asd',
            time='12:12'
        )
        super().setUpClass()

    def test_users_list(self):
        bd_users = User.objects.all()
        users_list = User.get_users_list()

        self.assertEqual(len(bd_users), len(users_list))

    def test_messages_list(self):
        bd_mess = Message.objects.all()
        mess_list = Message.get_messages_list()

        self.assertEqual(len(bd_mess), len(mess_list))

    def test_set_sended(self):
        self.assertFalse(self.message.is_sended)
        self.message.set_sended()
        self.assertTrue(self.message.is_sended)


class EmailSendViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.noauth_client = Client()
        cls.auth_client = Client()
        User.objects.create_user(username='estest', password='secret')
        cls.auth_client.login(username='estest', password='secret')
        cls.kwargs = {'time': '12:12', 'text': 'asd', 'email_to': 'a@a.com'}
        super().setUpClass()

    def test_noauth_send_get(self):
        response = self.noauth_client.get(reverse('email_send:send'))
        self.assertEqual(response.status_code, 302)

        response = self.noauth_client.get(reverse('email_send:send'), follow=True)
        self.assertEqual(urlparse(response.redirect_chain[-1][0]).path, reverse('login'))

    def test_noauth_send_post(self):
        response = self.noauth_client.post(reverse('email_send:send'), self.kwargs)
        self.assertEqual(response.status_code, 302)

        response = self.noauth_client.post(reverse('email_send:send'), self.kwargs, follow=True)
        self.assertEqual(urlparse(response.redirect_chain[-1][0]).path, reverse('login'))

    def test_auth_send_get(self):
        response = self.auth_client.get(reverse('email_send:send'))
        self.assertEqual(response.status_code, 200)

    def test_auth_send_post(self):
        response = self.auth_client.post(reverse('email_send:send'), self.kwargs)
        self.assertEqual(response.status_code, 302)

        response = self.auth_client.post(reverse('email_send:send'), self.kwargs, follow=True)
        self.assertEqual(response.redirect_chain[-1][0], reverse('email_send:sended'))
