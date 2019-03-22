from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class IndexView(generic.ListView):
	template_name = 'forum/index.html'

	def get_queryset(self):
		return Post.objects.all()


class DetailView(generic.DetailView):
	model = Post
	template_name = 'forum/detail.html'


class PostCreate(CreateView):
	model = Post
	fields = ['title', 'content', 'image']

class PostUpdate(UpdateView):
	model = Post
	fields = ['title', 'content', 'image']

class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('forum:index')