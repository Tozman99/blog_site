from django.contrib import admin
from .models import Post, Comment_Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	
	fields = ("title", "slug", "post", "auteur")
	prepopulated_fields = {"slug":("title",)}

@admin.register(Comment_Post)
class Comment_PostAdmin(admin.ModelAdmin):

	fields = ["comment", "post", "likes", "auteur_comment"]
	list_display = ["comment"]

	

