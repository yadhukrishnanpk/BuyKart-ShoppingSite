from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import SignupForm,LoginForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages

def index(request):
    items = Item.objects.filter(is_sold=False)
    Categories = Category.objects.all()
    context={
        'categories': Categories,
        'items' : items
    }
    return render(request, 'core/index.html', context)

def Signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registation Successful! Please Login.")
            return redirect('login')
        else:
            messages.error(request,"Registarion Failed.Enter valid Credentials")
    else:
        form = SignupForm()
    return render(request, "core/signup.html",{'form': form})
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method =='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,f"You are Logged in as {user.username}")
            return redirect('index')
        else:
            messages.error(request, "Invalid Username and Password")
    else:
        form = LoginForm()
    return render(request, "core/login.html", {'form': form})

def logout_view(request):
    storage = get_messages(request)
    for message in storage:
        pass
    logout(request)
    messages.success(request, "You have successfully logged out.Please Login")
    return redirect('login')



