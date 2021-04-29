from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	""" a Post the author is working on"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		""" represents the date the Post was published """
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		""" a string representation of the post title """
		return self.title

# Create your models here.
