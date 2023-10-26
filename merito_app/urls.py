from django.urls import path
from merito_app.views import test_response
from django.shortcuts import render
from . import views

urlpatterns = [
    path("test/", test_response),
    path('', views.test_response, name='test_response'),
]

def all_articles(request):
    title_page = "To jest tytuł strony"
    return render(
        request,
        'articles.html',
        {'title': title_page}
    )