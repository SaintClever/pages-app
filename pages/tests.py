from django.test import TestCase # for testing applications with a database

# Create your tests here.
from django.test import SimpleTestCase # for cases when we want to test an application. SimpleTestCase is for no database applications

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)