from django.contrib import admin
from django.urls import path,include
from git_book import views

urlpatterns = [
    path('/login',views.login),

]