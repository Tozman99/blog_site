from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import Post_Serializer, Comment_Post_Serializer
from Post_app.models import Post, Comment_Post
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from User_app.models import Profile
# Create your views here.


class Post_ViewSet(ModelViewSet):

	serializer_class = Post_Serializer
	queryset = Post.objects.all()
	lookup_field = "slug"
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	#throttle_scope = "post"
	#throttle_classes = (ScopedRateThrottle, )
	filter_fields = ("title", "auteur")
	search_fields = ("^title", )
	ordering_fields = ("title", "date")

	def perform_create(self, serializer):
        
		profile_obj = get_object_or_404(Profile, user=self.request.user)
		serializer.save(auteur=profile_obj)

class Comment_Post_ViewSet(ModelViewSet):

	serializer_class = Comment_Post_Serializer
	queryset = Comment_Post.objects.all()
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
        
		profile_obj = get_object_or_404(Profile, user=self.request.user)
		serializer.save(auteur_comment=profile_obj)




