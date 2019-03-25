from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    username = models.CharField('Username', max_length=60, unique=True)
    email = models.EmailField('E-mail', unique=True)
    birth_date = models.DateField('Birth Date', auto_now=False, null=True)

    description = models.TextField('Description', null=True, blank=True)
    Prof_pic = models.ImageField('Profile Picture', upload_to='user_prof_pic', null=True, blank=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    works_out = models.CharField('Works out at', max_length=60)
    city = models.CharField('Lives in', max_length=60)
    hometown = models.CharField('Hometown', max_length=60)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    object = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + self.last_name or self.username
