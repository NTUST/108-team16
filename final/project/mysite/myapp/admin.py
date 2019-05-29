from django.contrib import admin
from .models import account
# Register your models here.
class accountAdmin(admin.ModelAdmin):
	list_display = ('account','nickname')

admin.site.register(account,accountAdmin)