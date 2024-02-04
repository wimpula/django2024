from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Kysymys

def index(request):
    latest_question_list = Kysymys.objects.order_by("-julkaisupvm")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "kyselyt/index.html", context)

def yksityiskohdat(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def tulokset(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def äänestä(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
