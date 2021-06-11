from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import login
from django.urls import reverse
from .users.forms import RegisterForm, EditProfileForm
# Create your views here.

def dashboard(request):
    return render(request, 'users/dashboard.html')

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
            return redirect(reverse('dashboard'))

def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'users/edit_profile.html', {'form': form})

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form':form})