from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment
from accounts.models import User
from posts.forms import PostForm, CommentForm
from accounts.forms import UserRegisterForm, UserRegisterUpdateForm
from django.core.files.uploadedfile import SimpleUploadedFile
import json
from django.conf import settings
from model_mommy import mommy


class TestAccountsForms(TestCase):
    
    def setUp(self):
        self.client = Client()

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('Password123')
        self.user.save()

        self.index_url = reverse('index')
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.update_reg_url = reverse('accounts:my_account', args=[15])


    def test_login_ok(self):
        response = self.client.get(self.login_url)
        data = {
            'username': self.user.email, 
            'password': 'Password123',
        }
        response = self.client.post(self.login_url, data)
        redirect_url = reverse('index')
        self.assertRedirects(response, redirect_url)

    def test_register_form_data(self):
        form = UserRegisterForm(
            data = {
                'first_name': 'Gustavo', 
                'last_name' : 'Gasparini', 
                'username'  : 'gustavo',
                'email'     : 'gustavo@email.com',
                'password1' : 'Oliveira146',
                'password2' : 'Oliveira146',
                'birth_date': '20/02/1990',
                'gender'    : 'M',
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_ok(self):
        self.user.delete()
        response = self.client.get(self.register_url)
        data = {
            'first_name': 'Gustavo', 
            'last_name' : 'Gasparini', 
            'username'  : 'gustavo',
            'email'     : 'gustavo@email.com',
            'password1' : 'Oliveira146',
            'password2' : 'Oliveira146',
            'birth_date': '20/02/1990',
            'gender'    : 'M',
        }
        response = self.client.post(self.register_url, data)
        redirect_url = reverse('login')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(User.object.count(), 1)

    def test_update_register_form_data(self):
        upload_file = open('core/static/img/SJ-background.jpg', 'rb')
        file_image = SimpleUploadedFile(upload_file.name, upload_file.read())
        form = UserRegisterUpdateForm(
            data={
                'first_name': 'Gustavo',
                'last_name': 'Gasparini',
                'description': 'Lorem ipsum dolor sit a met',
                'description_card': 'Lorem ipsum dolor sit a met',
                'works_out': 'BlueFit',
                'last_gym': 'SmartFit',
                'city': 'Goiânia',
                'hometown': 'Conchal',
                'birth_date': '1990-02-20',
                'gender': 'M',
            },
            files={
                'Prof_pic': file_image,
                'cover_image': file_image,
            }
        )
        self.assertTrue(form.is_valid())

    def test_update_register_ok(self):
        self.client.login(username=self.user.email, password='Password123')
        User.object.create(pk=15)
        response = self.client.get(self.update_reg_url)
        upload_file = open('core/static/img/SJ-background.jpg', 'rb')
        file_image = SimpleUploadedFile(upload_file.name, upload_file.read())
        data = {
            'first_name': 'Gustavim',
            'last_name': 'Gaspareto',
            'description': 'ipsum dolor sit a met',
            'description_card': 'Lorem ipsum sit a met',
            'works_out': 'BlueFit',
            'last_gym': 'SmartFit',
            'city': 'Goiânia',
            'hometown': 'Conchal',
            'birth_date': '1990-02-20',
            'gender': 'M',
            'Prof_pic': file_image,
            'cover_image': '',
        }
        response = self.client.post(self.update_reg_url, data)
        redirect_url = reverse('accounts:profile', args=[15])
        self.assertRedirects(response, redirect_url)
