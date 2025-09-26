
# File: views.py
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: this file is my views for mini insta, assigment 3

from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from .models import Article --> from example
from .models import Profile
import random



class ProfileListView(ListView): 
    ''' Define a view class to display all users'''
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single profile'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    # method

    # def get_object(self):
    #     '''return one instance of the article object selected at random'''

    #     all_articles = Article.objects.all()
    #     article = random.choice(all_articles)
    #     return article 



# Create your views here.
# class ShowAllView(ListView): 
#     ''' Define a view class to display all blog Articles'''
#     model = Article
#     template_name = "mini_insta/show_all.html"
#     context_object_name = "articles"

# class ArticleView(DetailView):

#     model = Article
#     template_name = "mini_insta/article.html"
#     context_object_name = "article" #Note singular variable name

# class RandomArticleView(DetailView):
#     '''Display' a single article'''

#     model = Article
#     template_name = "mini_insta/article.html"
#     context_object_name = "article"

#     # method

#     def get_object(self):
#         '''return one instance of the article object selected at random'''

#         all_articles = Article.objects.all()
#         article = random.choice(all_articles)
#         return article 




