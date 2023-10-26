from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Article
# Create your views here.

def test_response(request):
    # Initialize HttpRequest with a single argument
    http_request = HttpRequest()
    return HttpResponse("Hello, World!")

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