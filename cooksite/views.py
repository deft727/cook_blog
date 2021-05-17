from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        print(self.kwargs.get("slug"))
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'



# def home(request):
#     return render(request,'base.html')