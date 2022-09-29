from django.shortcuts import render

from .models import Article


def articles_list(request):
    ordering = '-published_at'
    template = 'news.html'
    article = Article.objects.all().order_by(ordering)
    context = {
        'object_list': article
    }

    return render(request, template, context)