from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import profile_page, about_page, photos_page, add_photos_page, my_account_page, change_password, delete_post_prof_page

class TestUrls(SimpleTestCase):

    def test_profile_page_url_resolves(self):
        url = reverse('accounts:profile', args=[14])
        self.assertEquals(resolve(url).func, profile_page)

    def test_about_page_url_resolves(self):
        url = reverse('accounts:about', args=[14])
        self.assertEquals(resolve(url).func, about_page)

    def test_photos_page_url_resolves(self):
        url = reverse('accounts:photos', args=[14])
        self.assertEquals(resolve(url).func, photos_page)

    def test_add_photos_page_url_resolves(self):
        url = reverse('accounts:add-photos', args=[14])
        self.assertEquals(resolve(url).func, add_photos_page)

    def test_my_account_page_url_resolves(self):
        url = reverse('accounts:my_account', args=[14])
        self.assertEquals(resolve(url).func, my_account_page)

    def test_change_password_url_resolves(self):
        url = reverse('accounts:change_password', args=[14])
        self.assertEquals(resolve(url).func, change_password)

    def test_delete_post_prof_page_url_resolves(self):
        url = reverse('accounts:delete_post_prof', args=[14])
        self.assertEquals(resolve(url).func, delete_post_prof_page)