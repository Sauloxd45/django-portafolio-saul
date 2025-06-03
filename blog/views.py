from django.shortcuts import render,get_object_or_404
from.models import Post
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Estos 2 son los que faltaban 👇
from django.conf import settings
import os

# Create your views here.

def render_posts(request):
    posts = Post.objects.all()
    video = get_object_or_404(Post, id=1)
    return render(request, 'posts.html', {'posts': posts})
@xframe_options_sameorigin
def post_detail(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
