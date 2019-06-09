from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name",'last_name', "email", )

#       def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.Firstname = self.cleaned_data["First name"]
#         user.Lastname = self.cleaned_data["Last name"]
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

# class RegisterForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ("username", "email")