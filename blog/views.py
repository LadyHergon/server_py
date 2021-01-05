from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .sound import Sound

def home(request):
    context ={
        'posts' :Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10        #How many item per page

class UserPostListView(ListView):
    model = Post
    template_name ='blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10        #How many item per page

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','audio']

    def form_valid(self, form):
        form.instance.author =self.request.user
        
        SoundResult =  Sound(form.instance.audio)
        form.instance.image = SoundResult[0]
        form.instance.duration = SoundResult[1]
        form.instance.samp_freq = SoundResult[2]
        #form.instance.f_size = SoundResult[3]
        # form.instance.f_type = Ftype(form.instance.audio)
        
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content','audio']

    def form_valid(self, form):
        form.instance.author =self.request.user
        SoundResult =  Sound(form.instance.audio)
        form.instance.image = SoundResult[0]
        form.instance.duration = SoundResult[1]
        form.instance.samp_freq = SoundResult[2]
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        #check is the post author is the user
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        #check is the post author is the user
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
