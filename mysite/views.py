from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def contact(request):
    return render(request, 'contact.html')


@csrf_exempt
def faq(request):
    return render(request, 'faq.html')


@csrf_exempt
def team(request):
    return render(request, 'team.html')

@csrf_exempt
def features(request):
    return render(request, 'features.html')

