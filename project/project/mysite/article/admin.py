from django.contrib import admin
from .models import Article,Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','content')
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user','content')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)