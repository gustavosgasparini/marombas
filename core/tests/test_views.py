from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from model_mommy import mommy


class TestCoreViews(TestCase):
    
    def setUp(self):
        self.client = Client()

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.register_url = reverse('register')
        self.index_url =  reverse('index')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_register_test_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_index_test_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logout_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_login_GET(self):
        response2 = self.client.get(self.login_url)
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, 'registration/login.html')
        