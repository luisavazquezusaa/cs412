from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
import random

# Create your views here.
class ShowAllView(ListView): 
    ''' Define a view class to display all blog Articles'''
    model = Article
    template_name = "mini_insta/show_all.html"
    context_object_name = "articles"

class ArticleView(DetailView):

    model = Article
    template_name = "mini_insta/article.html"
    context_object_name = "article" #Note singular variable name

class RandomArticleView(DetailView):
    '''Display' a single article'''

    model = Article
    template_name = "mini_insta/article.html"
    context_object_name = "article"

    # method

    def get_object(self):
        '''return one instance of the article object selected at random'''

        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article 




