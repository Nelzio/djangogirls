from django.shortcuts import render

def blog(request):
    data = {}
    return render(request, 'blog/index.html', data)