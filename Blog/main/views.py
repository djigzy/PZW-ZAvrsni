from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *


def index(request):
    return render(request, 'index.html')

class KorisnikList(ListView):
    model = Korisnik
    
class ReputacijaList(ListView):
    model = Reputacija
    
class BlogList(ListView):
    model = Blog
    
class KomentarList(ListView):
    model = Komentar

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def noviKorisnik(request):
    if request.POST:
        form = noviKorisnikForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("main:index")
    form = noviKorisnikForm()
    return render(request, "main/formaNoviKorisnik.html", {'form':noviKorisnikForm})

def novaReputacija(request):
    if request.POST:
        form = novaReputacijaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("main:index")
    form = novaReputacijaForm()
    return render(request, "main/formaNovaReputacija.html", {'form':novaReputacijaForm})

def noviKomentar(request):
    if request.POST:
        form = noviKomentarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("main:index")
    form = noviKomentarForm()
    return render(request, "main/formaNoviKomentar.html", {'form':noviKomentarForm})

def noviBlog(request):
    if request.POST:
        form = noviBlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("main:index")
    form = noviBlogForm()
    return render(request, "main/formaNoviBlog.html", {'form':noviBlogForm})