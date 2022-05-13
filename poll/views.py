from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Question

# Create your views here.


def poll(request):
    query = {
    	'question': Question.objects.all(),

    }
    return render(request, 'poll/poll.html', query)

def detail(request, question_id = 0):
    query = {
    	'question_id': question_id,
    	'detail': Question.objects.filter(id = question_id),
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

