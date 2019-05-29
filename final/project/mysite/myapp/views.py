from django.shortcuts import render_to_response
from django.shortcuts import render
from myapp.models import account
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.
@csrf_exempt
def regist(request):
	if request.method =='POST':
		accounts = account.objects.all()
		acc = request.POST.get('acc')
		psw = request.POST.get('psw')
		email = request.POST.get('email')
		nickname = request.POST.get('nickname')
		account.objects.create(account = acc, password = psw , email=email,nickname=nickname)
		return HttpResponseRedirect('/login')
	else:
		return render_to_response('regist.html')

@csrf_exempt
def login(request):
	if request.method =='POST':
		acc = request.POST.get('acc')
		psw = request.POST.get('psw')
		try:
			user = account.objects.get(account = acc)
			if user.password == psw:
				request.session['is_login'] = True
				request.session['user_name'] = user.nickname
				request.session['user_account'] = user.account
				message = "successful"
				return HttpResponseRedirect('/index')
			else:
				message = 'wrong'
		except:
			message = "none"
		return render(request,"login.html",locals())
		alert(message)

	else:
		return render_to_response('login.html')
	
def logout(request):
	accounts = account.objects.all()
	

def index(request):
	accounts = account.objects.all()
	return render_to_response('index.html')

def member(request):
	accounts = account.objects.all()
	return render_to_response('member center.html')



def article(request):
	accounts = account.objects.all()
	return render_to_response('article.html')

def applePie(request):
	accounts = account.objects.all()
	return render_to_response('apple pie.html')

def chocolateCake(request):
	accounts = account.objects.all()
	return render_to_response('chocolate cake.html')

def coffeeCake(request):
	accounts = account.objects.all()
	return render_to_response('coffee cake.html')

def snowQCookie(request):
	accounts = account.objects.all()
	return render_to_response('snow Q cookie.html')

def tiramisu(request):
	accounts = account.objects.all()
	return render_to_response('tiramisu.html')

def strawberryCheeseCake(request):
	accounts = account.objects.all()
	return render_to_response('strawberry cheese cake.html')