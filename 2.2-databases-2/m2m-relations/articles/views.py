from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    print('articles:', articles)
    # context = {}
    # for article in articles:
    #     scopes = article.scopes.all()
    #     print(scopes)
    #     for scope in scopes:
    #         # print(scope.is_main)
    #         print(scope.tag.name)
    for article in articles:
        print('article:', article)
        print('article.scopes:', article.scopes)
        print('article.scopes.all:', article.scopes.all())
        for scope in article.scopes.all():
            print('scope.tag.name:', scope.tag.name)
    context = {'object_list': articles}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
