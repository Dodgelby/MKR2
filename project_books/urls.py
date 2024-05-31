"""
URL configuration for project_books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from books import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('ordered_books/', views.ordered_books, name='ordered_books'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book-list/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]