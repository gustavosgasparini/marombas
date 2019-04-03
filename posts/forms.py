from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    text = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {
            'class': 'form-control form-edit mb-3',
            'cols': 30,
            'rows': 3,
        }
    ))

    image = forms.ImageField(widget=forms.FileInput(
        attrs = {
            'class': 'custom-file-input',
            'id': 'inputGroupFile04',
            'aria-describedby': 'inputGroupFileAddon04',
        }
    ))

    class Meta:
        model = Post
        fields = ['text', 'image']


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs = {
            'class': 'form-control form-edit mb-3',
            'cols': 30,
            'rows': 3,
        }
    ))

    class Meta:
        model = Comment
        fields = ['text']
