from django.urls import path
from dapp import views

urlpatterns = [
    path('', views.homepage),
    path('home/', views.homepage, name='home'),
    path('items/', views.itempage, name='items'),
    path('about_me/', views.aboutme, name='about_me'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.register, name='register'),
]
