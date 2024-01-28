from os import name
from django.shortcuts import render


def blog(request):
    print('home do blog')

    context = {
        'text': 'Olá BLOG'
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):
    print('exemplo do blog')

    context = {
        'text': 'Olá EXEMPLO',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
