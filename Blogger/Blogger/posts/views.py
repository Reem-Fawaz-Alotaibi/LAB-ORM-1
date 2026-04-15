from django.shortcuts import render, redirect, get_object_or_404
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


def detail_post(request, id):
    post = get_object_or_404(Post, id=id)

    first_post = Post.objects.all().order_by('-published_at').first()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'first_post': first_post
    })


def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_published = request.POST.get('is_published') == 'on'
        post.save()
        return redirect('detail_post', id=post.id)

    return render(request, 'posts/update_post.html', {'post': post})



def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'posts/delete_post.html', {'post': post})