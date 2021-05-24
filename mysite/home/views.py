from django.shortcuts import redirect,render
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponse
from .users.forms import RegisterForm
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def esbelus(request):
    return HttpResponse("Outra mensagem")

def register(request):
    if request.method == 'GET':
        return render(
            request, 'users/register.html',
            {'form': RegisterForm}
        )
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))