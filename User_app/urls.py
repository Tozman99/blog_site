from django.urls import path, include
from .views import home_view, Wait_Confirm_View
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import User_Registration_View, profile_View, profile_other_user
from django.conf import settings
from django.conf.urls.static import static

app_name = "User_app"

urlpatterns = [
	
	#path("", home_view, name="home"),
	path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
	path("registration/", User_Registration_View, name="registration"),
	path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
	path("wait_confirm/", Wait_Confirm_View, name="wait-confirm"),
	path("accounts/profile/", profile_View, name="profile"),
	path("change-password/", auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("User_app:password_change_done")), name="Change_password"),
	path("change-password/done", auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),
	path("accounts/<int:id>/", profile_other_user, name="Other_User_View"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)