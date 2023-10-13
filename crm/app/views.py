from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm,CreateBookForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from app.models import Book

# Create your views here.
def home(request):
  return render(request,'app/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'form':form}
    return render(request, 'app/register.html', context=context) 
#login
def my_login(request):
  
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            #username = request.POST.get('username')
            username = request.POST['username']
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
               auth.login(request, user)
               return redirect("dashboard")
    form=LoginForm()
    context={'form':form}
    return render(request,"app/my-login.html",context)

# - User logout

def user_logout(request):

    auth.logout(request)

    #messages.success(request, "Logout success!")

    return redirect("my-login")

      
# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Book.objects.all()

    context = {'records':my_records}

    return render(request, 'app/dashboard.html', context=context)

@login_required(login_url='my-login')
def create_record(request):

    form = CreateBookForm()

    if request.method == "POST":

        form = CreateBookForm(request.POST)

        if form.is_valid():

            form.save()

            # messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'app/create-record.html', context=context)