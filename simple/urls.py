from django.urls import path
from .views import index, register

app_name = 'simple'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
]