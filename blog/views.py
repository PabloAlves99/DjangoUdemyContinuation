# pylint: disable=all
from typing import Any

from django.http import HttpRequest, Http404
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


def post(request: HttpRequest, post_id: int):
    FOUND_POST: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == post_id:
            FOUND_POST = post
            break

    if FOUND_POST is None:
        raise Http404('Post não existe.')

    context = {
        # 'text': 'Olá BLOG',
        'post': FOUND_POST,
        'title': FOUND_POST['title'],
    }

    return render(
        request,
        'blog/post.html',
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
