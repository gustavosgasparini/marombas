from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
@login_required
def PostPage(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post=post).order_by('-created')

    if request.method == 'POST':
        form_post = CommentForm(request.POST or None)
        if form_post.is_valid():
            content = request.POST.get('text')
            form = Comment.objects.create(post=post, author=request.user, text=content)
            form.save()
            return redirect('posts:post_page', pk)
    else:
        form_post = CommentForm()
    
    context = {
        'post': post,
        'comment': comment,
        'form_post': form_post,
        'total_likes': post.total_likes(),
    }
    return render(request, 'post.html', context)


@login_required
def like_post(request):
    post = get_object_or_404(Post, pk=request.POST.get('post_id'))

    is_liked = False
    if post.likes.filter(pk=request.user.pk).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponse('<script>history.back();</script>')


@login_required
def delete_commment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('posts:post_page', comment.post.pk)

    context = {'comment': comment}
    return render(request, 'delete_comment.html', context)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {'post': post}
    return render(request, 'delete_post.html', context)

