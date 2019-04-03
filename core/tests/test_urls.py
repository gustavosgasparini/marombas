from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import IndexPage, RegisterView
from django.contrib.auth.views import LoginView, LogoutView

class TestUrls(SimpleTestCase):

    def test_IndexPage_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, IndexPage)

    def test_RegisterView_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterView)

    def test_LoginView_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_LogoutView_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)