from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from wghw.email_sender.models import Message, User


class UsersAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_ok(self):
        response = self.client.get(reverse('api:users'))
        self.assertEqual(response.status_code, 200)

    def test_users_answer(self):
        db_users = User.objects.all()
        response = self.client.get(reverse('api:users'))

        users = response.json().get('users')
        self.assertEqual(len(users), len(db_users))


class MessageAPITestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.user = User.objects.create(username='messtest', email='messtest@test.com')
        cls.message = Message.objects.create(
            user=cls.user,
            email_to='a@a.com',
            text='asd',
            time='12:12'
        )
        super().setUpClass()

    def test_status_ok(self):
        response = self.client.get(reverse('api:messages'))
        self.assertEqual(response.status_code, 200)

    def test_messages_answer(self):
        response = self.client.get(reverse('api:messages'))

        answer = response.json().get('messages')
        self.assertEqual(len(answer), 1)
        self.assertEqual(answer[0]['status'], 'Ожидает')

    def test_message_status(self):
        self.message.set_sended()
        response = self.client.get(reverse('api:messages'))

        answer = response.json().get('messages')
        self.assertEqual(answer[0]['status'], 'Отправлено')
