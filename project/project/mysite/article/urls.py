"""class123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('articleCreate/',views.articleCreate,name='articleCreate' ),
    path('articleRead/<str:articleTitle>/',views.articleRead, name='articleRead'),
    path('articleDelete/<str:articleTitle>/', views.articleDelete, name='articleDelete'),
    path('commentCreate/<str:articleTitle>/', views.commentCreate, name= 'commentCreate'),
    path('commentDelete/<int:commentId>/', views.commentDelete, name='commentDelete'),
    path('index/',views.index, name='index'),
    path('articleLike/<str:articleTitle>/', views.articleLike, name='articleLike'),
    path('myArticle', views.myArticle, name='myArticle'),
    path('myLike', views.myLike, name='myLike'),


]
