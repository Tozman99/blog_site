from django.forms import ModelForm
from .models import Post, Comment_Post
from django import forms 


class Post_Form(ModelForm):

	class Meta:

		model = Post 
		fields = ["title", "post", "slug","auteur"]


class Comment_Form(ModelForm):
	class Meta:
		
		model = Comment_Post
		exclude = ["post", "auteur_comment", "likes"]