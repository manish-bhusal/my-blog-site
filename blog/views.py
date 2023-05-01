from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def starting_page(request):
    return render(request, 'blog/home.html')


def posts(request):
    return HttpResponse('posts page')


def post_detail(request):
    return HttpResponse('post detail page')
