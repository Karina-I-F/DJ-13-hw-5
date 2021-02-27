from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'

    context = {'object_list': Article.objects.all().order_by('-published_at'),
               'scopes': Relationship.objects.all().order_by('-main', '-category')}

    return render(request, template, context)
