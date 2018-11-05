from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Bruno Kanazawa', cpf='12345678901',
                    email='kanazawabruno@gmail.com', phone='19-99245-2648')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        """"""
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """"""
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """"""
        expect = ['contato@eventex.com.br', 'kanazawabruno@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """"""

        contents = ['Bruno Kanazawa',
                    '12345678901',
                    'kanazawabruno@gmail.com',
                    '19-99245-2648']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
