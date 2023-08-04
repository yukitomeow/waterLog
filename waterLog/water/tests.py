from django.test import TestCase
from django.http import HttpRequest
from water.views import top


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")
class TopNewViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/water/new/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/water/new/")
        self.assertEqual(response.content, b"top new")