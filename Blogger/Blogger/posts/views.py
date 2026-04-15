from django.shortcuts import render, redirect
from .models import Post

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published') == 'on'

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published
        )

        return redirect('home') 

    return render(request, 'posts/add_post.html')