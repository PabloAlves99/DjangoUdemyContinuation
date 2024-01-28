from django.shortcuts import render


def home(request):
    print('home do app')

    context = {
        'text': 'Estamos na home',
        'title': 'Home do Pablo',
    }

    return render(
        request,
        'home/index.html',
        context
    )
