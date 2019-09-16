from django.shortcuts import render
from .models import Post

def blog(request):
    data = {}
    data['posts'] = Post.objects.all()
    return render(request, 'blog/index.html', data)