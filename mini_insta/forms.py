# File: forms.py 
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/02/2025
# Description: forms file for the app mini_insta

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm): 
        '''A form to add a comment about an article'''

        image_url = forms.URLField(required=False, label="Image URL")

        class Meta: 
                '''associate this form with a model from our database'''
                model = Post
                #fields = ['profile', 'username', 'bio_text'] #deleated
                fields = ['caption', 'image_url'] #we dont want the drop down list


#Examples Assignment 4:

        # class CreateArticleForm(forms.ModelForm): 
        #     """ a Form to add an article to the """

        #     class Meta:
        #         """associate this from with a model from out data base"""
        #         model = Profile
        #         fields = ['username', 'display_name', 'bio_text', 'profile_image_url']

        # class CreateCommentForm(forms.ModelForm): 
        #     '''A form to add a comment about an article'''

        #     class Meta: 
        #         '''associate this form with a model from our database'''
        #         model = Comment
        #         fields = ['profile', 'username', 'bio_text'] #deleated
        #         fields = ['username', 'bio_text'] #we dont want the drop down list