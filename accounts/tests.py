import json
import requests
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Message


class MessageTestCase(TestCase):
    """Тестирование создания объектов Message"""
    def setUp(self):
        Message.objects.create(mail_from="user@ya.ru", note="note text")
        Message.objects.create(mail_from="staff@ya.com", note="message")
        Message.objects.create(mail_from="Julianne.OConner@kory.org", note="word")

    def test_note_is_correct(self):
        """Проверка содержимого дополняемого в отправленом сообщении"""

        def parse(email):
            user_list = json.loads(
                (requests.get('http://jsonplaceholder.typicode.com/users')).text
            )
            for user in user_list:
                if email in user:
                    return f'\n\n{json.dumps(user)}'
            return ''

        from_user = Message.objects.get(mail_from="user@ya.ru")
        from_staff = Message.objects.get(mail_from="staff@ya.com")
        from_vip_user = Message.objects.get(
            mail_from="Julianne.OConner@kory.org"
        )
        self.assertEqual(from_user.note, 'note text')
        self.assertEqual(from_staff.note, 'message')
        self.assertEqual(
            from_vip_user.note,
            'word' + parse("Julianne.OConner@kory.org")
        )


class UrlTest(TestCase):
    """Тест доступности урлов"""
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.user = User.objects.create_user(
            username='admin',
            email='mail@aa.aa',
            password='123'
        )

    def test_login_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        """Проверка на редирект"""
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_registration_url(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)

    def test_sending_url(self):
        """Проверка на редирект"""
        response = self.client.get('/sending/')
        self.assertEqual(response.status_code, 302)
