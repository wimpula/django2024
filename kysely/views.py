from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Moro. Oot kysely-appin index-sivul.")

def yksityiskohdat(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def tulokset(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def äänestä(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
