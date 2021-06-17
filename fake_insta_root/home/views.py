from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from .users.forms import RegisterForm, EditProfileForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'users/dashboard.html'
    ordering = ['-post_date']

    #def get_context_data(self, *args, **kwargs):
    #    
    #    context = super(HomeView, self).get_context_data(*args, **kwargs)
    #    current_post = get_object_or_404(Post, id=self.kwargs.get('pk'))
    #    total_likes = current_post.total_likes
    #    context['total_likes'] = total_likes
    #    return context

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
        form = EditProfileForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form':form})

class AddPostView(CreateView):
    model = Post
    template_name = 'users/add_post.html'
    fields = '__all__'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    #return redirect('dashboard')
    if request.is_ajax():
        return HttpResponse(liked, request)