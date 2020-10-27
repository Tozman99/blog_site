from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
from allauth.account.forms import SignupForm
from django import forms



class User_Form(UserCreationForm):



	class Meta:

		model = User 
		fields = ["username", "password1", "password2", "email",
					"first_name", "last_name"]

		widgets={
            'username': forms.TextInput(attrs={"class":"inputField"}),
            'password1': forms.PasswordInput(attrs={'class': 'inputField'}),
			'password2': forms.PasswordInput(attrs={'class': 'inputField'}),
			"email": forms.EmailInput(attrs={'class': 'inputField'}),
			'first_name': forms.TextInput(attrs={'class': 'inputField'}),
            'last_name': forms.TextInput(attrs={'class': 'inputField'}),

        }


class Profile_Form(ModelForm):


	class Meta:

		model = Profile
		exclude = ["user"]


class Signupallauth(SignupForm):

	def save(self, request):

		user = super(Signupallauth, self).save(request)
		Profile.objects.create(user=user)
		print(user)
		return user
