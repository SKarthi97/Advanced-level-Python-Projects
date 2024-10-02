from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="tracker/base.html"), name="tracker"),
    path('logout/', auth_views.LogoutView.as_view(template_name="tracker/logout.html"), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name="tracker/login.html"), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]