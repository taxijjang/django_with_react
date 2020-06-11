from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

def home(request):
    return render(request,'home.html')

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     return render(request, 'instagram/post_list.html',{
#         'post_list' : qs,
#         'q' : q,
#     })

# post_list = login_required(ListView.as_view(model = Post, paginate_by = 10))

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 9

post_list = PostListView.as_view()
def post_detail(request, pk):
    pass