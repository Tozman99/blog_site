from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from .models import Post, Comment_Post
from django.views.generic.edit import FormView
from .forms import Post_Form, Comment_Form
from User_app.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.forms import modelform_factory
from django.views.generic import FormView
from django.views import View
from django.http.request import QueryDict


# Create your views here.



@login_required
def posts_user(request):
	obj = get_object_or_404(Profile, user=request.user.id)
	posts = Post.objects.filter(auteur=obj)

	return render(request, "Post_app/posts_list_user.html", {"posts_user":posts})


class Post_List_View(ListView):

	model = Post
	#paginate_by = 2
	#ordering = ["-date"]
	template_name = "Post_app/list.html"

	def queryset(self):
		
		return Post.objects.all()

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		
		query_key = "q"
		get_url_kwargs = self.request.GET.get(query_key)
		if get_url_kwargs:
			
			context["object"] = Post.objects.filter(title__contains=get_url_kwargs)
			#print(context["object"], self.request.GET.get(query_key))

		else:
			context["object"] = Post.objects.all()
		

		return context


class Post_Detail_View(DetailView):

	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		obj_profile = get_object_or_404(Profile, user=self.request.user.id)
		context["profile_object"] = obj_profile
		context["Comment_Form"] = Comment_Form()
		context["Comments"] = Comment_Post.objects.filter(post=self.object)
		print(self.kwargs)

		return context 

class Post_Form_CreateView(LoginRequiredMixin, CreateView):
	
	model = Post
	fields = ["title", "post"]

	def form_valid(self, form):
		current_user = self.request.user 
		obj = get_object_or_404(Profile, user=current_user.id)	
		form.instance.auteur = obj

		return super().form_valid(form)

	def get_success_url(self, **kwargs):

		return reverse('Post_app:Detail_Post', kwargs={"slug": self.object.slug})

class Post_Form_UpdateView(UpdateView):

	model = Post
	fields = ["title", "post"]
	template_name_suffix = "_update_form"

	def get_success_url(self, **kwargs):

		return reverse("Post_app:Detail_Post", kwargs={"slug":self.object.slug})

class Post_Form_DeleteView(DeleteView):

	model = Post
	success_url = reverse_lazy("Post_app:list_post")


def search_post(request):
	
	postForm = modelform_factory(Post, exclude=("post", "slug", "auteur"))
	form = postForm()
	objs = Post.objects.all()
	if request.method == "POST":
		form = postForm(request.POST)
		
		if form.is_valid():
			objs = Post.objects.filter(title__contains=request.POST["title"])

			return render(request, "Post_app/search_post.html", {"form_search": form, "objects":objs})
	
	return render(request, "Post_app/search_post.html", {"form_search":form, "objects":objs})
	

class Comment_View(SingleObjectMixin, FormView):

	form_class = Comment_Form
	model = Post

	def post(self, request, *args, **kwargs):
		
		if not request.user.is_authenticated:

			pass
		self.object = self.get_object()
		
		return super().post(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("Post_app:Detail_Post", kwargs={"slug":self.object.slug})

	def form_valid(self, form):
		form.instance.post = self.object 
		form.instance.auteur_comment = get_object_or_404(Profile, user=self.request.user.id)
		form.save()

		return super().form_valid(form)

class Detail_View(View):

	def get(self, request, *args, **kwargs):
		
		view = Post_Detail_View.as_view(template_name="Post_app/detail.html")
		
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):

		view = Comment_View.as_view(template_name="Post_app/detail.html")

		return view(request, *args, **kwargs)
