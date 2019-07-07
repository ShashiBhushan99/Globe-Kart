from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Account has been created')
			return redirect('blog-home')
	else:
		form=UserRegisterForm()
	return render(request,'user/boot_register.html',{ 'form':form })
@login_required	
def profile(request):
    return render(request, 'profile.html')	

# Create your views here.
