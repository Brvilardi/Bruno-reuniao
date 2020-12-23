from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.login, name = "login"),
    path('login_post', views.login_post, name="login_post"),
    path('switch', views.switch, name="switch"),
]