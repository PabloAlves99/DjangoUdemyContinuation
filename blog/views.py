from django.shortcuts import render


def blog(request):
    print('home do blog')

    return render(
        request,
        'blog/index.html',
    )


def exemplo(request):
    print('exemplo do blog')

    return render(
        request,
        'blog/exemplo.html',
    )
