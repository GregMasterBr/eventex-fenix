from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase): # Cenário de teste (O TestCase herda do Unit Test)
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return satatus code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')        
   
    def test_subscription_link(self):
            expected = 'href="{}"'.format(r('subscriptions:new'))
            self.assertContains(self.response, expected)   
    
    