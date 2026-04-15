from django.shortcuts import render
from posts.models import Post

def home(request):
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': latest_posts})