# pylint: disable=all
from blog.data import posts
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá BLOG',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, id):
    print(id)

    context = {
        # 'text': 'Olá BLOG',
        'posts': posts
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
