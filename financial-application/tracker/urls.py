from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name="tracker/base.html"), name="tracker"),
    path('login/', auth_views.LoginView.as_view(template_name="tracker/login.html"), name='login'),
]