from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Moro. Oot kysely-appin index-sivul.")

