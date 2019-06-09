from django.db import models
from myapp.models import User
import django.utils.timezone as timezone

# Create your models here.
class Article(models.Model):
	author = models.CharField(max_length=32, default = '')
	title = models.CharField(max_length=128, unique=True)
	content = models.TextField(blank=True)
	videoID = models.CharField(max_length=256, blank=True)
	material = models.TextField()
	step1 = models.TextField(blank=True)
	pubDateTime = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User)
	img = models.ImageField(default = '',blank=True,upload_to='images')

	def _str_(self):
		return self.title
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	content = models.TextField()
	pubDateTime = models.DateTimeField(auto_now_add=True)
	def _str_(self):
		return self.content