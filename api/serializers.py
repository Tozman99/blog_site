from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField, ModelSerializer, HyperlinkedRelatedField
from Post_app.models import Post, Comment_Post
from rest_framework import serializers 
from rest_framework.request import Request


class Comment_Post_Serializer(ModelSerializer):
	
	auteur_comment = serializers.ReadOnlyField(source='auteur.user.username')

	class Meta:
		
		model = Comment_Post
		fields = ['comment', 'post', 'auteur_comment', "date"]
		context={'request': Request}


class Post_Serializer(HyperlinkedModelSerializer):
	
	auteur = serializers.ReadOnlyField(source='auteur.user.username')
	comments = Comment_Post_Serializer(many=True, read_only=True)

	class Meta:

		model = Post
		fields = ["title", "auteur", "post", "url", "comments"]
		extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
		





