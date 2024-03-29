from django.test import TestCase
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm
from django.shortcuts import redirect, resolve_url as r
from django.core import mail


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        '''
        GET /inscricao must return status code 200
        '''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        '''
        Must use subscriptions/subscription_form.html
        '''
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ Html must contaim input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for tag, count in tags:
            with self.subTest():
                self.assertContains(self.response, tag, count)
  
    def test_crsf(self):
        """Html must contain csrf_token"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""

        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""

        form = self.response.context['form']
        self.assertSequenceEqual(
            ['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))
        data = dict(name='Gregorio Queiroz', cpf='12345678901',
                    email='gregmasterbr@gmail.com', phone='15-98105-7742')
        self.resp = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        '''
            Valid POST should redirect to /inscricao/
        '''
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, r('subscriptions:detail',1))

    def test_send_subscribe_email(self):
        ''' Valida se existe o e-mail   '''
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        '''Salva a instância no banco de dados'''
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''Must use subscriptions/subscription_form.html'''
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        '''Context must have subscription form'''
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        '''Form must contain errors'''
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        '''verifica se a instância não existe no banco de dados'''
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name="Gregorio Queiroz", cpf="12345678901")

        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response,'<ul class="errorlist nonfield">')