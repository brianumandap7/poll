from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User

# Create your views here.


def poll(request):
    query = {

    }
    return render(request, 'poll/poll.html', query)

