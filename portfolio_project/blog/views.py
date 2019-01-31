from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.order_by('-date_posted')
	context = {
		'posts':posts
	}
	return render(request,'blog/index.html',context=context)

def detail(request, post_title):
	post = get_object_or_404(Post, to_url=post_title)
	return render(request,'blog/detail.html',{'post':post})