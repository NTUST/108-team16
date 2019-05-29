from django.shortcuts import render_to_response
from django.shortcuts import render
from myapp.models import account
# Create your views here.
def index(request):
	accounts = account.objects.all()
	return render_to_response('index.html')

def member(request):
	accounts = account.objects.all()
	return render_to_response('member center.html')

def login(request):
	accounts = account.objects.all()
	return render_to_response('login.html')

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