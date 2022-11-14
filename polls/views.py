from django.shortcuts import render
from django.db.models.manager import Manager
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
