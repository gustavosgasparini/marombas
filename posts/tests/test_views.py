from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment
from accounts.models import User
import json
from django.conf import settings
from model_mommy import mommy


class TestPostsViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.post_url = reverse('posts:post_page', args=[45])
        self.delete_comment_url = reverse('posts:delete_comment', args=[17])
        self.delete_post_url = reverse('posts:delete_post', args=[45])
        self.like_url = reverse('posts:like_post')

        self.post45 = Post.objects.create(author=self.user, pk=45)
        self.comment17 = Comment.objects.create(author=self.user, post=self.post45, text='This is a comment', pk=17)


    def test_post_page_GET(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_like_page(self):
        self.client.login(username=self.user.email, password='Password123')
        post = get_object_or_404(Post, pk=45)
        self.assertEquals(post.likes.count(), 0)
        post.likes.add(self.user)
        self.assertEquals(post.likes.count(), 1)
        post.likes.remove(self.user)
        self.assertEquals(post.likes.count(), 0)

    def test_delete_comment(self):
        self.client.login(username=self.user.email, password='Password123')
        self.comment17
        response = self.client.get(self.delete_comment_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_comment.html')
        comments = Comment.objects.filter()
        self.assertEquals(comments.count(), 1)
        response2 = self.client.post(self.delete_comment_url)
        self.assertEquals(response2.status_code, 302)
        self.assertEquals(comments.count(), 0)

    def test_delete_post(self):
        self.client.login(username=self.user.email, password='Password123')
        response = self.client.get(self.delete_post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')
        posts = Post.objects.all()
        self.assertEquals(posts.count(), 1)
        response2 = self.client.post(self.delete_post_url)
        self.assertEquals(response2.status_code, 302)
        self.assertEquals(posts.count(), 0)
