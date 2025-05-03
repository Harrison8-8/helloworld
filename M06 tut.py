


#Django Data In Templates

from django.shortcuts import render
from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

# Django Templates
#Everything is in HTML, so it wont translate right

#CSS make it Pretty

