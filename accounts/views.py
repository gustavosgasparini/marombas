from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserRegisterUpdateForm

# Create your views here.
@login_required
def profile_page(request, pk):
    one_user = get_object_or_404(User, pk=pk)
    context = {'one_user': one_user}
    return render(request, 'accounts/profile.html', context)

@login_required
def about_page(request, pk):
    one_user = get_object_or_404(User, pk=pk)
    context = {'one_user': one_user}
    return render(request, 'accounts/about.html', context)

@login_required
def photos_page(request, pk):
    one_user = get_object_or_404(User, pk=pk)
    context = {'one_user': one_user}
    return render(request, 'accounts/photos.html', context)

@login_required
def add_photos_page(request, pk):
    return render(request, 'accounts/add_photos.html')

@login_required
def my_account_page(request, pk):
    one_user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        form = UserRegisterUpdateForm(request.POST or None, request.FILES or None, instance=one_user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', pk)
    else:
        form = UserRegisterUpdateForm(instance=one_user)

    context = {
        'one_user': one_user,
        'form': form,
    }
    return render(request, 'accounts/my_account.html', context)
