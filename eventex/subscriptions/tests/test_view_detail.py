from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription

class SubscribeDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Gregorio Queiroz',
            cpf='12345678901',
            email='gregmasterbr@gmail.com',
            phone='15-981057742'
        )        
        self.resp = self.client.get(r('subscriptions:detail',self.obj.pk))
        #self.resp = self.client.get('/inscricao/1/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    
    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        #contents = ('Gregorio Queiroz','12345678901','gregmasterbr@gmail.com','15-981057742')
        contents = (self.obj.name,self.obj.cpf,self.obj.email,self.obj.phone)
                
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)
