from django.contrib import admin
from django.urls import path, re_path
from .views import ( 
						Post_List_View, 
						Post_Detail_View, 
						Post_Form_CreateView, 
						Post_Form_UpdateView,
						Post_Form_DeleteView,
						posts_user,
						search_post,
						Detail_View
					)
from .models import Post

app_name = "Post_app"

urlpatterns = [
    path("ViewPost", Post_List_View.as_view(), name="list_post"),
    path("createpost", Post_Form_CreateView.as_view(template_name="Post_app/createpost.html"), name="Post_Form"),
    path("YourPosts", posts_user, name="list_user_post"),
    path("ViewPost/<slug:slug>/", Detail_View.as_view(), name="Detail_Post"),
    path("ViewPost/<slug:slug>/update/", Post_Form_UpdateView.as_view(template_name="Post_app/post_update.html"), name="Post_Update"),
    path("ViewPost/<slug:slug>/delete/", Post_Form_DeleteView.as_view(template_name="Post_app/post_delete.html"), name="Post_Delete"),
    #path("search/", search_post, name="search_post"),
	re_path("search/(?P<slug>\w+)/$", search_post, name="search_post"),
    
]
