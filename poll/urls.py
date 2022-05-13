from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework.authtoken.views import obtain_auth_token



app_name = 'poll'
urlpatterns = [
    path('', views.poll, name='poll'),
    path('owner', views.owner, name='owner'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

