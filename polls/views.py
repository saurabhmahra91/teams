from multiprocessing import context
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, request
from .models import Question, Choice, User
from django.contrib import auth
from django.urls import reverse

def index(request):
    context = {'latest_question_list':Question.objects.order_by('-pub_date')[:5]}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    sorted_choices = q.choice_set.all().order_by('-votes')
    context = {
        "question":q,
        "choices": sorted_choices,
    }
    return render(request,'polls/result.html' , context)

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question':q, 'err':"you did not select any option!"}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(q.id, )))


def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
        context = {'question': q}
    except Question.DoesNotExist:
        raise Http404("No such Question exists")

    return render(request, 'polls/detail.html',context)

def authpage(request):
    return render(request, 'polls/authpage.html')


def signin(request):
    user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    auth.login(request, user)
    # return redirect(index)
    context = {}
    return render(request, 'polls/index.html', context)


def login(request):
    user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        print("USER FOUND")
        auth.login(request, user)
    context = {}
    return HttpResponseRedirect(reverse('polls:index'))
    return redirect(index) #error logging in
    return render(request, 'polls/index.html', context)







