from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
@login_required
def PostPage(request, pk):
    return render(request, 'post.html')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {'post': post}
    return render(request, 'delete_post.html', context)

