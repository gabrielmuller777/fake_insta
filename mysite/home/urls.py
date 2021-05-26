from django.urls import path
from django.conf.urls import include
from .views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls'))
]