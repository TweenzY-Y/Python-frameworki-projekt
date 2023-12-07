from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Article
# Create your views here.

def test_response(request):
    context = {
        'variable_name': 'Hello from Django!',  # You can pass data to the template here
    }
    return render(request, 'articles.html', context)

def all_articles(request):
    title_page = 'Tytuł strony'
    options = [
        "option 1",
        "option 2",
        "option 3"
    ]

    articles = Article.objecs.all()

    return render(
        request,
        'articles.html',
        {
            'title': title_page,
            'options': options,
            'articles': articles
        }
    )