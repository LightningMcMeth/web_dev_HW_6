from django.http import HttpResponse
from django.shortcuts import render
from hw_6.data import product

def testing(request):
    return HttpResponse("Very kind and nice words :)")