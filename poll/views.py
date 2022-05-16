from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Question, Choice
from django.db.models import F

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
        'cdetail': Choice.objects.filter(question_id = question_id),
    }

    if request.method == "POST":
        if request.POST.get('vt1') == "42":
            Choice.objects.filter(id = 1).update(votes=F('votes')+1)
        if request.POST.get('vt4') == "Something else":
            Choice.objects.filter(id = 4).update(votes=F('votes')+1)
        return HttpResponseRedirect('results/')
    return render(request, 'poll/detail.html', query)

def vote(request):
    query = {

    }
    return render(request, 'poll/poll.html', query)

def results(request, question_id = 0):
    query = {
        'question_id': question_id,
        'detail': Question.objects.filter(id = question_id),
        'cdetail': Choice.objects.filter(question_id = question_id),
    }
    return render(request, 'poll/results.html', query)

def owner(request):
       return HttpResponse("Hello, world. 6884af24 is the polls index.")

