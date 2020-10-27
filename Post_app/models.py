from django.db import models
from django.urls import reverse
from User_app.models import Profile 
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length=100)
	post = models.TextField()
	date = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True)
	auteur = models.ForeignKey(Profile, on_delete=models.CASCADE)


	def __str__(self):

		return self.title

	def get_queryset(self):

		return Post.objects.filter(auteur=auteur)

	def save(self, *args, **kwargs):

		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

class Comment_Post(models.Model):

	comment = models.TextField(max_length=200)
	date = models.DateField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	likes = models.PositiveIntegerField(default=0)
	auteur_comment = models.ForeignKey(Profile, on_delete=models.CASCADE)

	class Meta:

		ordering = ["date"]

	def __str__(self):

		return f"Comment from {self.post}"

