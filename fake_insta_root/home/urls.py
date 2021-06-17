from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from .views import HomeView, register, editProfile, AddPostView, LikeView

urlpatterns = [
    path('like/<int:pk>', LikeView, name='like_post'), 
    path('', login_required(HomeView.as_view()), name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit_profile/', editProfile, name='edit_profile'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]