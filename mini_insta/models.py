
# File: models.py
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 09/25/2025
# Description: this file is my models for mini insta, assigment 4

from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self): 
        '''Return a URL to displya one instance of this object.'''
        return reverse('profile', kwargs={'pk': self.pk})
    
    def get_all_posts(self):
        '''Return a QuerySet of Posts about this Profile'''
        #Used the object manager to retrieve comments about this article
        
        posts = Post.objects.filter(profile=self)
        return posts

    
class Post(models.Model): 
    '''Encapsulate the idea of a comment in an Article'''

    # data atributes for the Post:
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True) #tells when comment was written 

    def __str__(self):
        '''Return a string representation of this comment'''
        return f'{self.caption}'
    
    def get_all_photos(self):
        """Return a QuerySet of Photos for this Post, ordered by timestamp"""
        photos = Photo.objects.filter(post=self).order_by('-timestamp')
        return photos

    

class Photo(models.Model): 
    '''Encapsulate the idea of a comment in an Article'''

    # data atributes for the Post:
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True) #tells when comment was written 
    image_url = models.URLField(blank = True)

    def __str__(self):
        '''Return a string representation of this comment'''
        return f'{self.timestamp}'
    


#from examples, Assingnment 4

        # class Comment(models.Model): 
        #     '''Encapsulate the idea of a comment in an Article'''

        #     # data atributes for the Comment:
        #     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        #     username = models.TextField(blank=False)
        #     bio_text = models.TextField(blank=False)
        #     published = models.DateTimeField(auto_now=True) #tells when comment was written 

        #     def __str__(self):
        #         '''Return a string representation of this comment'''
        #         return f'{self.text}'



# Code from the example assigment 3: 

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



