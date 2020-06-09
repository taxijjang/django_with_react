from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

def home(request):
    return render(request,'home.html')

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(message__icontains=q)

    return render(request, 'instagram/post_list.html',{
        'post_list' : qs,
        'q' : q,
    })

def post_detail(request, pk):
    pass