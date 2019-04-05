from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment
from accounts.models import User
from posts.forms import PostForm, CommentForm
from django.core.files.uploadedfile import SimpleUploadedFile
import json
from django.conf import settings
from model_mommy import mommy


class TestPostsForms(TestCase):
    
    def setUp(self):
        self.client = Client()

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.index_url = reverse('index')
        self.post_url = reverse('posts:post_page', args=[45])
        self.post45 = Post.objects.create(author=self.user, pk=45)

    def test_post_form_valid(self):
        upload_file = open('core/static/img/SJ-background.jpg', 'rb')
        file_image = SimpleUploadedFile(upload_file.name, upload_file.read())
        form = PostForm( 
            data={'text': 'Lorem ipsum dolor sit a met',}, 
            files={'image': file_image,}
        )
        self.assertTrue(form.is_valid())

    def test_post_ok(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.index_url)
        upload_file = open('core/static/img/SJ-background.jpg', 'rb')
        file_image = SimpleUploadedFile(upload_file.name, upload_file.read())
        data = {
            'text': 'Lorem Ipsum Dolor Sit a met',
            'image': file_image,
        }
        response = self.client.post(self.index_url, data)
        redirect_url = reverse('index')
        self.assertRedirects(response, redirect_url)

    def test_comment_form_valid(self):
        form = CommentForm(
            data={
                'text': 'Lorem ipsum dolor sit a met',
            }
        )
        self.assertTrue(form.is_valid())

    def test_comment_ok(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.post_url)
        data = {
            'text': 'Lorem Ipsum Dolor Sit a met', 
        }
        response = self.client.post(self.post_url, data)
        redirect_url = reverse('posts:post_page', args=[45])
        self.assertRedirects(response, redirect_url)

    def test_comment_form_nodata(self):
        form = CommentForm(data={'text': '',})
        error = {'text': ['This field is required.']}
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, error)

    def test_post_form_nodata(self):
        form = PostForm( 
            data={'text': '',}, 
            files={'image': '',}
        )
        error = {'image': ['This field is required.']}
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors, error)
