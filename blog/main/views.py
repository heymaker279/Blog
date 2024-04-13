from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404, HttpResponse


def post_list(request):
    posts = Post.published.all()
    # return HttpResponse(posts)
    return render(request, 'main/post/list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    # return HttpResponse(post)
    return render(request, 'main/post/detail.html', {'post': post})