from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    print('home do app')
    return HttpResponse('home do app')
