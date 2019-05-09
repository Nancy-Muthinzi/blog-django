from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Nancy KM',
        'title': 'Blog Post 1',
        'content': 'Post Content 1',
        'date_posted': '01/01/2019'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'app1/home.html', context)

def about(request):
    return render(request, 'app1/about.html')
    