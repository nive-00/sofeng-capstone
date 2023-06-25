from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author':'niv',
        'title': 'post1',
        'content': 'first content',
        'date_posted': 'june 6,2023',
    },{
        'author':'jomar',
        'title': 'post2',
        'content': 'second content',
        'date_posted': 'june 8,2023',
    }
]
def home(request):
    return HttpResponse('<h1>Announcements</h1>')
    context = {
        'posts' : posts
    }
    return render(request, 'announcements/announcements.html',context)

def about(request):
    return HttpResponse('<h1>About</h1>')
    return render(request, 'announcements/about.html', {'title':'hello'})