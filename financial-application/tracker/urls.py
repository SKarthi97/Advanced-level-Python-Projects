from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="tracker/base.html"), name="tracker"),
    path('logout/', auth_views.LogoutView.as_view(template_name="tracker/logout.html"), name="logout"),
]