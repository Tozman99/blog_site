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
from django.shortcuts import redirect


def home_view(request):
	print(request)
	return render(request, "User_app/home.html", {})


def User_Registration_View(request):

	form = User_Form()

	if request.method == "POST":
		
		form = User_Form(request.POST)

		if form.is_valid():

			form.save()
			obj = get_object_or_404(User, username=request.POST["username"])

			Profile.objects.create(user=obj)

			user_mail = request.POST["email"]
			message = ("Hi", "This is an automated message", EMAIL_HOST_USER, [user_mail])
			send_mail("Hi ", "This is Your username: {} and your password {},\n you can now login to your account Here: http://127.0.0.1:8000/login/".format(request.POST["username"], request.POST["password1"]), EMAIL_HOST_USER, [user_mail])

			return HttpResponseRedirect("../login")

	return render(request, "registration/signup.html", {"form":form})
 

def profile_View(request):

	form = Profile_Form()
	obj = get_object_or_404(Profile, user=request.user.id)
	if request.method == "POST":
		
		form = Profile_Form(request.POST, request.FILES, instance=obj)
		if form.is_valid():

			obj.image = request.FILES["image"]
			form.save()		

	return render(request, "registration/profile.html", {"person":obj, "form":form})

@login_required(login_url="/login/")
def profile_logout_view(request):
	print("OK")
	return redirect("home_view", name="home")

def profile_other_user(request, id):

	user = get_object_or_404(Profile, pk=id)
	print(dir(user))
	return render(request, "registration/profile_other_user.html", {"user":user})

