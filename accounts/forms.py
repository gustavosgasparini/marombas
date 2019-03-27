from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class UserRegisterForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    birth_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y',))

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'birth_date', 'gender']


class UserRegisterUpdateForm(UserChangeForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Prof_pic = forms.ImageField(widget=forms.FileInput(
        attrs= {
            'class': '',
        }
    ))
    cover_image = forms.ImageField(widget=forms.FileInput(
        attrs= {
            'class': '',
        }
    ))
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'description', 'description_card', 'works_out', 'last_gym', 'city', 'hometown', 'birth_date', 'gender', 'Prof_pic', 'cover_image']