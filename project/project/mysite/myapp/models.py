from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(label = "Email")
#     Firstname = forms.CharField(label = "First name")
#     Lastname = forms.CharField(label = "Last name")
#     class Meta:
#         model = User
#         fields = ("username", "Firstname",'Lastname', "email", )

#       def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.Firstname = self.cleaned_data["First name"]
#         user.Lastname = self.cleaned_data["Last name"]
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user
# Create your models here.

# class account(models.Model):
# 	account = models.CharField(max_length=20,unique=True)
# 	password = models.CharField(max_length=20)
# 	email = models.EmailField(max_length=50)
# 	nickname = models.CharField(max_length=10)

# 	def __str__(self):
# 		return self.nickname
# 	class Meta:
# 		db_table='accounts'	
