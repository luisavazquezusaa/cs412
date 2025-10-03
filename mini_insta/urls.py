# File: urls.py 
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: Urls for the app mini_insta

from django.urls import path
# from .views import ShowAllView, RandomArticleView, ArticleView, --> from example
from .views import * 

urlpatterns = [

    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all_profiles/', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    #path('profile/<int:pk>/create_comment', ProfileDetailView.as_view(), name='profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name="create_post"),


    #examples assigment 4: 
    # path('profile/create', CreateArticleView.as_view(), name="create_article"),
    # path('create_comment', CreateCommentView.as_view(), name="create_comment"),

    #from example: 
    # path('', RandomArticleView.as_view(), name="random"),
    # path('show_all/', ShowAllView.as_view(), name="show_all"),
    # path('article/<int:pk>', ArticleView.as_view(), name='article')
]