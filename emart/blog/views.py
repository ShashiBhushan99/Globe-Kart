from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 

pts=[ { 'title':' ',
		'content':' ',
		'date_posted':' ',
		'author':' '
		}
	]
	
def post(request):
	context={
				'pts':Post.objects.all()#acess all the records from post database.
			}
	return render(request,'blog/post.html',context)
		
def home(request):
	return render (request,'blog/blog-home.html')
def login(request):
	return render (request,'blog/blog-login.html')
def about(request):
	return render(request,'blog/blog-about.html')
	
# Create your views here.
