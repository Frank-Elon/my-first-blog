""" Defines the url patterns for the blog """

from django.urls import path
from . import views


urlpatterns = [
	#Home page
	path('', views.post_list, name='post_list'),
]