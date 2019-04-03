from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import PostPage, like_post, delete_commment, delete_post


class TestUrls(SimpleTestCase):

    def test_PostPage_url_resolves(self):
        url = reverse('posts:post_page', args=[12])
        self.assertEquals(resolve(url).func, PostPage)
    
    def test_like_post_url_resolves(self):
        url = reverse('posts:like_post')
        self.assertEquals(resolve(url).func, like_post)

    def test_delete_comment_url_resolves(self):
        url = reverse('posts:delete_comment', args=[12])
        self.assertEquals(resolve(url).func, delete_commment)

    def test_delete_post_url_resolves(self):
        url = reverse('posts:delete_post', args=[12])
        self.assertEquals(resolve(url).func, delete_post)
