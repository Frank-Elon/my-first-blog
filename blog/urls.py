""" Defines the url patterns for the blog """

from django.urls import path
from . import views


urlpatterns = [
	#Home pagem shows all post
	path('', views.post_list, name='post_list'),
	#show details of a post
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	#Page for making new post
	path('post/new/', views.post_new, name='post_new'),
	#Page for editing existing post
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]