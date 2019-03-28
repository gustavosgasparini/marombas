from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserRegisterUpdateForm
from posts.forms import PostForm
from posts.models import Post

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required
def profile_page(request, pk):
    one_user = get_object_or_404(User, pk=pk)
    post = Post.objects.filter(author=one_user).order_by('-created')

    if request.method == 'POST':
        form_post = PostForm(request.POST or None, request.FILES or None)
        if form_post.is_valid():
            form = form_post.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('accounts:profile', pk)
    else:
        form_post = PostForm()

    context = {
        'one_user': one_user,
        'post': post,
        'form_post': form_post,
    }
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
    one_user = get_object_or_404(User, pk=pk)
    context = {'one_user': one_user}
    return render(request, 'accounts/add_photos.html', context)


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


@login_required
def change_password(request, pk):
    one_user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST or None, user=one_user)
        if form.is_valid():
            form.save()
            # to keep the user logged after change the password
            update_session_auth_hash(request, form.user) 
            return redirect('accounts:profile', pk)
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=one_user)

    context = {
        'one_user': one_user,
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)