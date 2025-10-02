
# File: views.py
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: this file is my views for mini insta 

from django.shortcuts import render
from django.views.generic import ListView, DetailView #CreateView
# from .models import Article --> from example
from .models import Profile, Post, Photo
import random
# from .forms import CreateArticleForm, CreateCommentForm    from example Assignment 4
from django.urls import reverse



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


class PostDetailView(DetailView):
    '''Display a single post'''

    model = Post 
    template_name = "mini_insta/show_post.html"
    context_object_name = "post" #Note singular variable name




#examples assigment 4: 

        # class CreateArticleView(CreateView):
        #     '''a view to handles creation of a new article
        #     (1) disaply the HTML form to the user (GET)
        #     (2) process the form submission and store the new Profile object (POST)
        #     '''

        #     form_class = CreateArticleForm 
        #     template_name = "mini_insta/create_article_form.html"

        # class CreateCommentView(CreateView): 
        #     '''a view to handle creation of a new Comment on a Profile'''

        #     form_class = CreateCommentForm
        #     template_name = "mini_insta/create_comment_form.html"

        #     def get_success_url(self):
        #         '''Provide a URL to redirect to after creating a new Comments'''

        #         #Create and return a URL: 
        #         return reverse('show_all_profiles')  #not ideal

            #     #retrive PK from the URL pattern 
            #     pk = self.kwargs['pk']

            #     #call reverseto generate the URL for this Profile
            #     return reverse('profile', kwargs={'pk':pk})  
                  
            # def get_context_data(self):
            #     '''Return the dictionary of context variables for use in the template.'''
        
            #     # calling the superclass method
            #     context = super().get_context_data()
        
        
            #     # find/add the article to the context data
            #     # retrieve the PK from the URL pattern
            #     pk = self.kwargs['pk']
            #     article = Article.objects.get(pk=pk)
        
        
            #     # add this article into the context dictionary:
            #     context['article'] = article
            #     return context

            # def form_valid(self, form): 
            #     '''This method handles the form submission and saves the 
            #     new object to the Django database.
            #     We need to add the foreign key (of the Article) to the Comment
            #     object before saving it to the database.
            #     '''
            #     #retrive PK from the URL pattern 
            #     pk = self.kwargs['pk']
            #     profile = Profile.objects.get(pk-pk)
            #     #attach this Profile to the comment 
            #     form.instance.profile = profile #set the FK

            #     #deleagte the work to the superclass method form_valid: 
            #     return super().form_valid(form)



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




