from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='home-page'),


path("about/", views.about, name="about"),

path("login/",views.login,name="login"),
    path("newuser/",views.newuser,name="newuser"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]