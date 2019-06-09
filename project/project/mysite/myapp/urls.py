from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('accounts/regist/', views.regist, name='regist'),
    path('accounts/logout/',views.logout, name='logout'),
    path('index/',views.index,name='index'),
    path('memberCenter/', views.member, name='member center'),
    path('accounts/login/', views.login , name="login"),
    path('article/', views.article , name="article"),
    path('apple_pie/', views.applePie, name="applePie"),
    path('chocolate_cake/', views.chocolateCake,name='chocolateCake'),
    path('coffee_cake/', views.coffeeCake,name='coffeeCake'),
    path('snow_Q_cookie/', views.snowQCookie,name='snowQCookie'),
    path('tiramisu/',views.tiramisu,name='tiramisu'),
    path('strawberry_cheese_cake/',views.strawberryCheeseCake,name='strawberryCheeseCake'),
    path('search/',views.search,name='search'),
]
