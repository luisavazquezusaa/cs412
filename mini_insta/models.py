
# File: models.py
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: this file is my models for mini insta, assigment 3

from django.db import models

# Create your models here.
    

class Profile(models.Model): 
    '''Model for the user profile '''

    # Define the data atributes

    username = models.TextField(blank = True)
    display_name = models.TextField(blank = True)
    bio_text = models.TextField(blank = True)
    join_date = models.DateTimeField(auto_now = True)
    profile_image_url = models.URLField(blank = True)

    def __str__(self): 
        '''return a string representation of the model instance.'''
        return f'{self.username} joined {self.join_date}'
    

# Code from the example: 

    # class Article(models.Model): 
#     ''' '''

#     # Define the data atributes

#     title = models.TextField(blank = True)
#     author = models.TextField(blank = True)
#     text = models.TextField(blank = True)
#     published = models.DateTimeField(auto_now = True) 
#     image_ulr = models.URLField(blank = True)


#     def __str__(self): 
#         '''return a string representation of the model isntance.'''
#         return f'{self.title} by {self.author}'



