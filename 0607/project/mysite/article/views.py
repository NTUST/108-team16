from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from article.forms import ArticleForm
from article.models import Article


# Create your views here.
def index(request):
	template= 'index.html'
	articles= Article.objects.all()
	context={'articles':articles}
	return render(request,template,context)
def articleCreate(request):
	template= 'article_1.html'
	if request.method == 'GET':
		return render(request,template,{'articleForm':ArticleForm()})
	articleForm = ArticleForm(request.POST)
	if not articleForm.is_valid():
		return render(request,template,{'articleForm':articleForm})
	author= request.POST.get('author')
	articleForm.save()
	# Article.objects.filter(title=title).update(author=author)

	messages.success(request,'文章已新增')
	return redirect('article:index')
def articleDelete(request,articleTitle):
	if request.method=='GET':
		return redirect('article:article')
	article = get_object_or_404(Article, title=articleTitle)
	article.delete()
	return redirect('article:index')
def articleRead(request,articleTitle):
	article = get_object_or_404(Article, title=articleTitle)
	context= {
	'article':article,
	}
	return render(request,'articleRead.html',context)