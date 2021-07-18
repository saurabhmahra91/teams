from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request
from .models import Question, Choice
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

