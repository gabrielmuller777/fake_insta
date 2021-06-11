from django.urls import path
from django.conf.urls import include
from .views import dashboard, register, editProfile

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit_profile/', editProfile, name='edit_profile')
]