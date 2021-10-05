from django.contrib.auth import authenticate, login, logout
from django.db.models.query_utils import refs_expression
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import register
from .forms import signupform, loginForm
# Create your views here.
def loginform(request):
  if request.method=="POST":
    form = loginForm(request=request, data=request.POST)
    if form.is_valid():
      uname = form.cleaned_data['username']
      upass = form.cleaned_data['password']
      user = authenticate(username=uname, password=upass)
      if user is not None:
        login(request, user)
        return redirect('/registration/')
  else:
    form = loginForm()
    return render(request, 'loginform.html', {'form':form})

def signup(request):
  if request.method=='POST':
    form = signupform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/login/')
  else:
    form = signupform()
  return render(request, 'signup.html', {'form':form})




def registration(request):
  reg = register(request.POST)
  if request.method == "POST":
    usr = request.user
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    city = request.POST['city']
    address = request.POST['address']
    reg = register(user = usr, firstname=firstname, lastname=lastname, email=email, address=address, city=city)
    reg.save()
    return redirect('/showdetails/')
  else:
    reg=register()
  return render(request, 'registration.html')


def showdetails(request):
  reg =  register.objects.filter(user=request.user)
  return render(request, 'showdetails.html',{'reg':reg})


def userlogout(request):
  logout(request)
  return redirect('/loginform/')


def edit(request, id):
  reg = register.objects.get(id=id)
  return render(request, 'edit.html', {'register':reg} )

def update(request, id):
  if request.method=="POST":
    reg = register.objects.filter(id=id)
    reg.update(
      firstname = request.POST['firstname'],
      lastname = request.POST['lastname'],
      email = request.POST['email'],
      address = request.POST['address'],
      city = request.POST['city'],
    )
    return redirect('/showdetails/')

def delete(request, id):
  reg = register.objects.get(id=id)
  reg.delete()
  return redirect('/showdetails/')