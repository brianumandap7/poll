from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User

# Create your views here.


def poll(request):
    query = {

    }
    return render(request, 'poll/poll.html', query)

def detail(request):
    query = {

    }
    return render(request, 'poll/detail.html', query)

def vote(request):
    query = {

    }
    return render(request, 'poll/poll.html', query)

def results(request):
    query = {

    }
    return render(request, 'poll/results.html', query)

def owner(request):
       return HttpResponse("Hello, world. 6884af24 is the polls index.")

