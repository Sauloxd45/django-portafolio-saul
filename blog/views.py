from django.shortcuts import render

# Create your views here.
def render_posts(request):
    return render(request, 'posts.html')