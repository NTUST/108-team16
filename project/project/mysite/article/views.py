from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from article.forms import ArticleForm
from article.models import Article,Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	template= 'index.html'
	articles= Article.objects.all()
	context={'articles':articles}
	return render(request,template,context)
@login_required
def articleCreate(request):
	template= 'article_1.html'
	if request.method == 'GET':
		return render(request,template,{'articleForm':ArticleForm()})
	articleForm = ArticleForm(request.POST)
	if not articleForm.is_valid():
		return render(request,template,{'articleForm':articleForm})
	articleForm.save()
	# Article.objects.filter(title=title).update(author=author)

	# messages.success(request,'文章已新增')
	# return redirect('article:index')
	return HttpResponseRedirect('/index/?message=create_successful')
def articleDelete(request,articleTitle):
	if request.method=='GET':
		return redirect('article:article')
	article = get_object_or_404(Article, title=articleTitle)
	article.delete()
	return redirect('article:index')
def articleRead(request,articleTitle):
	article = get_object_or_404(Article, title=articleTitle) 
	author = str(article.author)
	user = str(request.user)
	condition = request.user in article.likes.all()
	context= {
	'article':article,
	'comments':Comment.objects.filter(article=article),
	'author':author,
	'user':user,
	'condition':condition,
	}
	return render(request,'articleRead.html',context)
def commentCreate(request,articleTitle):
	if request.method =='GET':
		return articleRead(request,articleTitle)
	comment = request.POST.get('comment')
	if comment:
		comment = comment.strip()
	if not comment:
		return redirect('article:articleRead', articleTitle=articleTitle)
	article = get_object_or_404(Article, title=articleTitle)
	Comment.objects.create(user=request.user, article= article, content= comment)
	return redirect('article:articleRead', articleTitle=articleTitle)
def commentDelete(request,commentId):
	comment = get_object_or_404(Comment,id=commentId)
	article = get_object_or_404(Article, title=comment.article.title)
	if request.method == 'GET':
		return articleRead(request,article.title)
	if comment.user != request.user:
		messages.error(request,"刪除發生錯誤")
		return redirect('article:articleRead',articleTitle=article.title)
	comment.delete()
	return redirect('article:articleRead',articleTitle=article.title)
def articleLike(request,articleTitle):
	article = get_object_or_404(Article,title=articleTitle)
	if request.user  in article.likes.all():
		article.likes.remove(request.user)
		return articleRead(request,articleTitle)	
	article.likes.add(request.user)
	return articleRead(request,articleTitle)

def myArticle(request):
	template = 'myArticle.html'
	articles=Article.objects.filter(author=str(request.user))
	context={
	'articles':articles,
	}
	return render(request,template,context)

def myLike(request):
	template='myLike.html'
	articles=Article.objects.filter(likes = request.user)
	context={
	'articles':articles,
	}
	return render(request,template,context)