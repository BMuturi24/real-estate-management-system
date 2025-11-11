from django.test import TestCase
from django.urls import reverse


class PropertiesSmokeTest(TestCase):
    def test_list_properties(self):
        resp = self.client.get('/api/properties/')
        self.assertIn(resp.status_code, (200, 301, 302))