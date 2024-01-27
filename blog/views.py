from django.http import HttpResponse
# from django.shortcuts import render


def blog(request):
    print('blog do app')
    return HttpResponse('blog do app')
