
from django.urls import path, include 
from .views import Post_ViewSet, Comment_Post_ViewSet
from rest_framework.routers import DefaultRouter, url
from Post_app.models import Comment_Post
from .serializers import Comment_Post_Serializer
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()


router.register("posts", Post_ViewSet)
router.register("comments", Comment_Post_ViewSet)
post_list = Post_ViewSet.as_view({"get":"list", "post":"create"})
post_detail = Post_ViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})
comment_list = Comment_Post_ViewSet.as_view({"get": 'list', "post":"create"})
comment_detail = Comment_Post_ViewSet.as_view(
				{"get":"retrieve", "put":"update", "delete":"destroy"}

								)
comment_update = Comment_Post_ViewSet.as_view({"get":"retrieve", "put":"update"})
comment_delete = Comment_Post_ViewSet.as_view({"get":"retrieve", "delete":"destroy"})

urlpatterns = [
		path("posts/", post_list, name="post-list"),
		path("posts/<slug:slug>/", post_detail, name="post-detail"),
        path("posts/<post_slug>/<int:pk>/", comment_detail, name="Comment_Post-detail"),
        path("comments/", comment_list, name="Comment_Post-list"),

		
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])

#urlpatterns = router.urls
