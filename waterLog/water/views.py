from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return HttpResponse(b"Hello World")

def top_new(request):
    return HttpResponse(b"top new")
