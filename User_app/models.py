from django.db import models
from django.contrib.auth.models import User
import glob, os 
from PIL import Image
# Create your models here.

class Profile(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="media/photo_profile/", default="nopicture.jpeg")

	
	def __str__(self):

		return self.user.username

	def get_queryset(self):

		return self.user.objects.all() 

	def get_object(self):

		return self.user

	
	def save(self, **kwargs):

		super().save()

		size = 40, 40
		image = Image.open(self.image.path)
		image.thumbnail(size)
		image.save(self.image.path)

