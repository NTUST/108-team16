from django.db import models

# Create your models here.
class Article(models.Model):
	author = models.CharField(max_length=32, default='')
	title = models.CharField(max_length=128, unique=True)
	content = models.TextField(blank=True)
	videoID = models.CharField(max_length=256, blank=True)
	material = models.TextField()
	step1 = models.TextField(blank=True)
	def _str_(self):
		return self.title