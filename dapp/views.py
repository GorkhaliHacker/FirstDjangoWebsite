from django.shortcuts import render, redirect
from dapp.models import Item
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def homepage(request):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, template_name='hypertml/home.html', )


def itempage(request):
    if request.method == 'GET':
        allitems = Item.objects.all()
        return render(request, template_name='hypertml/items.html', context={'allitems': allitems})
    if request.method == 'POST':
        purchased_item = request.POST['purchased-item']
        if purchased_item:
            purchased_item_object = Item.objects.get(name=purchased_item)
            purchased_item_object.stock = purchased_item_object.stock - 1
            purchased_item_object.owner = request.user
            purchased_item_object.save()
            print('Congratulations')
            messages.info(request, f'Thank You For Purchasing {purchased_item_object}')

        return redirect('items')





def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='hypertml/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('items')
        else:
            messages.info(request, 'Invalid Credientials')
            return redirect('login')
    else:
        return render(request, template_name='hypertml/login.html')


def logoutpage(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        return render(request, template_name='hypertml/register.html')
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                print('Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                print("Email ALready Taken")
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'Congratulations, You have Succesfully Registered Your Account')
                print('User Created')
        else:
            messages.info(request, 'Passwords Does Not Match')
            print('Password Not Matched')
            return redirect('register')

        return redirect('login')


def aboutme(request):
    return render(request, template_name='hypertml/about_me.html')