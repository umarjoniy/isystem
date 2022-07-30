from django.shortcuts import render
from curslar.models import Courses


def home(request):
    return render(request,'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    posts = Courses.objects.filter(is_published = True)
    context = {
        'posts' : posts
    }
    return render(request,'courses.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name,email,message)

    return render(request,'contact.html',{})

def add(request,a,b):
    pass

def one_page(request,slug):
    post = Courses.objects.get(slug=slug)
    context = {
        'post':post
    }
    return render(request,'one_page.html',context)