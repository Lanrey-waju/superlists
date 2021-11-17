from django.http.request import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpResponse, response

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        req = HttpRequest()
        response = home_page(req)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
