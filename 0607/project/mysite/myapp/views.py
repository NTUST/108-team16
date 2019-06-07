from django.shortcuts import render_to_response
from django.shortcuts import render
# from myapp.models import account
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from article.models import Article
from django.db.models.query_utils import Q


@csrf_exempt
def login(request):
	if request.user.is_authenticated: 
		return HttpResponseRedirect('/index/?message=already')
	if request.method =='POST': #接收到submit指令則驗證登入
		acc = request.POST.get('acc')
		psw = request.POST.get('psw')
		user = auth.authenticate(username=acc, password=psw)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/index/?message=successful')
		else:
			return HttpResponseRedirect('/accounts/login/?message=error') 
	else: #接收到submit指令則進入登入頁面
 		return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')


@csrf_exempt
def regist(request):
	if request.user.is_authenticated: 
		return HttpResponseRedirect('/index/?message=already') 	
	if request.method =='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/accounts/login/?message=successful')
		else:
			form = RegisterForm()
			return HttpResponseRedirect('/accounts/regist/?message=error') 
	else:
		form = RegisterForm()
		return render_to_response('regist.html',locals())

# Create your views here.
# @csrf_exempt
# def regist(request):
# 	if request.method =='POST':
# 		accounts = account.objects.all()
# 		acc = request.POST.get('acc')
# 		psw = request.POST.get('psw')
# 		email = request.POST.get('email')
# 		nickname = request.POST.get('nickname')
# 		account.objects.create(account = acc, password = psw , email=email,nickname=nickname)
# 		return HttpResponseRedirect('/login')
# 	else:
# 		return render_to_response('regist.html')

# @csrf_exempt
# def login(request):
# 	if request.method =='POST':
# 		acc = request.POST.get('acc')
# 		psw = request.POST.get('psw')
# 		try:
# 			user = account.objects.get(account = acc)
# 			if user.password == psw:
# 				request.session['is_login'] = True
# 				request.session['user_nickname'] = user.nickname
# 				request.session['user_account'] = user.account
# 				message = "successful"
# 				return HttpResponseRedirect('/index/?message=successful')
# 			else:
# 				message = 'wrong'
# 				return HttpResponseRedirect("/login/?message=error")
# 		except:
# 			message = "none"
# 		return HttpResponseRedirect("/login/?message=error")
		

# 	else:
# 		return render_to_response('login.html')
	
# def logout(request):
# 	accounts = account.objects.all()
	

def index(request):
	# accounts = account.objects.all()
	articles= Article.objects.all()
	return render_to_response('index.html',locals())

@login_required
@csrf_exempt
def member(request):
	# accounts = account.objects.all()
	return render_to_response('member center.html',locals())


@login_required
def article(request):
	# accounts = account.objects.all()
	return render_to_response('article_1.html',locals())

def applePie(request):
	# accounts = account.objects.all()
	return render_to_response('apple pie.html',locals())

def chocolateCake(request):
	# accounts = account.objects.all()
	return render_to_response('chocolate cake.html',locals())

def coffeeCake(request):
	# accounts = account.objects.all()
	return render_to_response('coffee cake.html',locals())

def snowQCookie(request):
	# accounts = account.objects.all()
	return render_to_response('snow Q cookie.html',locals())

def tiramisu(request):
	# accounts = account.objects.all()
	return render_to_response('tiramisu.html',locals())

def strawberryCheeseCake(request):
	# accounts = account.objects.all()
	return render_to_response('strawberry cheese cake.html',locals())

def search(request):
	if request.method == 'GET':
		searchText = request.GET.get('search', '')
		articles = Article.objects.filter(Q(title__icontains=searchText)|Q(material__icontains=searchText))
	return render_to_response('articleSearch.html',locals())