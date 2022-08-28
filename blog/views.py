from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    #posts = Post.objects.filter(published_at__lte=timezone.now())
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    context = {"post": post}
    return render(request, "blog/post-detail.html", context)

