from django.test import TestCase
from django.urls import reverse


class AccountsSmokeTest(TestCase):
def test_register_endpoint(self):
resp = self.client.post(reverse('register'), data={'username': 'u', 'password': 'p'})
self.assertIn(resp.status_code, (200,201,400))