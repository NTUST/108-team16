from django.db import models

# Create your models here.
class account(models.Model):
	account = models.CharField(max_length=20,unique=True)
	password = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	nickname = models.CharField(max_length=10)

	def __str__(self):
		return self.nickname