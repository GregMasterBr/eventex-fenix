from django.test import TestCase


class HomeTest(TestCase): # Cenário de teste (O TestCase herda do Unit Test)
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return satatus code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')        