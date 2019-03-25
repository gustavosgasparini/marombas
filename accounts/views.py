from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile_page(request, pk):
    return render(request, 'accounts/profile.html')

@login_required
def about_page(request, pk):
    return render(request, 'accounts/about.html')

@login_required
def photos_page(request, pk):
    return render(request, 'accounts/photos.html')

@login_required
def add_photos_page(request, pk):
    return render(request, 'accounts/add_photos.html')

@login_required
def my_account_page(request, pk):
    return render(request, 'accounts/my_account.html')
