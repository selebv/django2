from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm

def indexViews(request):
    return render(request, 'home.html')

def aboutViews(request):
    return render(request, 'about.html')

def registroViews(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'registro.html', context)


def loginViews(request):
    return render(request, 'login.html')


