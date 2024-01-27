from django.shortcuts import render


def home(request):
    print('home do app')

    return render(
        request,
        'home/index.html',
    )
