from django.shortcuts import render,redirect, get_object_or_404
from .forms import User_Form, Profile_Form
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail, send_mail
from Blog.settings import EMAIL_HOST_USER
from .models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PIL import Image

def home_view(request):
	print(request)
	return render(request, "User_app/home.html", {})

def resize_image(self, picture):

		image = picture.resize((30, 30))

		return image 


def User_Registration_View(request):

	form = User_Form()

	if request.method == "POST":
		form = User_Form(request.POST)

		if form.is_valid():

			form.save()
			obj = get_object_or_404(User, username=request.POST["username"])

			Profile.objects.create(user=obj)

			user_mail = request.POST["email"]
			message = ("Hello there", "This is an automated message", EMAIL_HOST_USER, [user_mail])

			send_mail("Hello there", "Hello, This is Your username: {} and your password {}".format(request.POST["username"], request.POST["password1"]), EMAIL_HOST_USER, ["karim.sadiki@gmail.com"])

			#return redirect("login")
			return HttpResponseRedirect("../login")

	return render(request, "registration/signup.html", {"form":form})
 
	
	#else:
	#	return render(request, "registration/signup.html", {"form":form})
		

def Wait_Confirm_View(request):
	
	message = ("Hello there", "This is an automated message", EMAIL_HOST_USER, ["karim.sadiki@gmail.com"])

	send_mass_mail(message)

	return render(request, "registration/wait_confirm", {})


def profile_View(request):

	form = Profile_Form()
	obj = get_object_or_404(Profile, user=request.user.id)
	if request.method == "POST":
		
		form = Profile_Form(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			print(request.FILES)
			obj.image = request.FILES["image"]
			#picture = request.FILES["file"]
			#resize_image(picture)
			form.save()		

			

	return render(request, "registration/profile.html", {"person":obj, "form":form})

@login_required(login_url="/login/")
def profile_logout_view(request):

	return render(request, "registration/logout.html", {})

def profile_other_user(request, id):

	user = get_object_or_404(Profile, pk=id)
	print(dir(user))
	return render(request, "registration/profile_other_user.html", {"user":user})

