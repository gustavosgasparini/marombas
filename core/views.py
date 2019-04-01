from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from accounts.forms import UserRegisterForm
from posts.forms import PostForm

from accounts.models import User
from posts.models import Post, Comment
from django.db.models import Count

# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


@login_required
def IndexPage(request):
    post = Post.objects.order_by('-created')

    # This post something in the index
    if request.method == 'POST':
        form_post = PostForm(request.POST or None, request.FILES or None)
        if form_post.is_valid():
            form = form_post.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('index')
    else:
        form_post = PostForm()

    is_liked = False
    if Post.objects.filter(likes=request.user.pk):
        is_liked = True

    context = {
        'post': post,
        'form_post': form_post,
        'is_liked': is_liked,
    }
    return render(request, 'index.html', context)
