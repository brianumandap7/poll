from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.authtoken.views import obtain_auth_token



app_name = 'schema'
urlpatterns = [
  path('', views.poll, name='poll'),
]

