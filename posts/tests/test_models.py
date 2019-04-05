from django.test import TestCase, Client
from posts.models import Post, Comment
from accounts.models import User
from django.conf import settings
from model_mommy import mommy
from django.utils import timezone
import datetime
from unittest import mock
import pytz


class TestPostsModels(TestCase):

    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.post45 = Post.objects.create(author=self.user, pk=45)


    def test_timezone_created_now(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            post = Post.objects.create(author=self.user, pk=15)
            self.assertEquals(post.created, timezone.now())
    
    def test_user_author_post(self):
        new_user = User.object.create(pk=15)
        new_post = Post.objects.create(author=new_user, pk=25)
        self.assertEquals(new_post.author, new_user)

    def test_user_author_and_post_same(self):
        another_user = User.object.create(pk=16)
        another_post = Post.objects.create(author=self.user, pk=35)
        comment = Comment.objects.create(author=another_user, post=another_post)
        self.assertEquals(comment.post, another_post)
        self.assertEquals(comment.author, another_user)
