# File: urls.py 
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: Urls for the app mini_insta
from django.urls import path
from .views import ShowAllView, RandomArticleView, ArticleView

urlpatterns = [
    path('', RandomArticleView.as_view(), name="random"),
    path('show_all/', ShowAllView.as_view(), name="show_all"),
    path('article/<int:pk>', ArticleView.as_view(), name='article')
]