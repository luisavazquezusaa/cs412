# File: urls.py 
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: Urls for the app mini_insta

from django.urls import path
# from .views import ShowAllView, RandomArticleView, ArticleView, --> from example
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('show_all_profiles/', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name="create_post"),
    #path('profile/,int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    #path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),


    #examples assigment 4: 
    # path('profile/create', CreateArticleView.as_view(), name="create_article"),
    # path('create_comment', CreateCommentView.as_view(), name="create_comment"),

    #from example: 
    # path('', RandomArticleView.as_view(), name="random"),
    # path('show_all/', ShowAllView.as_view(), name="show_all"),
    # path('article/<int:pk>', ArticleView.as_view(), name='article')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)