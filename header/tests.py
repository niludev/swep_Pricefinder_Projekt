from django.test import TestCase

# When there is no database
from django.test import SimpleTestCase

from django.urls import reverse

# Create your tests here.

class HeaderPageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/header/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('header'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('header'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('header'))
        self.assertContains(response, '<h1>Hello World.</h1>')
