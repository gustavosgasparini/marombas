from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment
from accounts.models import User
import json
from django.conf import settings
from model_mommy import mommy


class TestAccountsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.profile_url = reverse('accounts:profile', args=[25])
        self.profile_page = User.object.create(pk=25)
        self.about_url = reverse('accounts:about', args=[25])
        self.photos_url = reverse('accounts:photos', args=[25])        
        self.add_photos_url = reverse('accounts:add-photos', args=[25])
        self.my_account_url = reverse('accounts:my_account', args=[25])
        self.change_password_url = reverse('accounts:change_password', args=[25])
        self.delete_post = reverse('accounts:delete_post_prof', args=[45])

    def test_profile_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_about_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/about.html')

    def test_photos_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.photos_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/photos.html')

    def test_add_photos_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.add_photos_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/add_photos.html')

    def test_my_account_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.my_account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/my_account.html')

    def test_change_password_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.change_password_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/change_password.html')

    def test_delete_post_page(self):
        self.client.login(username=self.user.email, password='Password123')
        posts = Post.objects.all()
        self.assertEquals(posts.count(), 0)
        self.post45 = Post.objects.create(author=self.user, pk=45)
        self.assertEquals(posts.count(), 1)
        response = self.client.get(self.delete_post)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/delete_post_prof.html')
        response2 = self.client.post(self.delete_post)
        self.assertEquals(response2.status_code, 302)
        self.assertEquals(posts.count(), 0)
