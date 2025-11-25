# File: models.py
# Author: Luisa Vazquez Usabiaga (lvu@bu.edu), 11/23/2025
# Description: Models for subletting marketplace application.

from django.db import models
from django.urls import reverse
# Create your models here.


class UserProfile(models.Model):
    '''User profile for the platform'''

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)   
    bio = models.TextField(blank=True)
    image_file = models.ImageField(upload_to='profile_images/', blank=True, null=True) 
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''readable representation of this profile.'''
        return f'{self.display_name} ({self.username})'

    def get_absolute_url(self):
        '''Return URL to display this profile.'''
        return reverse('userprofile', kwargs={'pk': self.pk})

    def get_listings(self):
        '''Return all listings created by this user.'''
        from .models import Listing
        return Listing.objects.filter(lister=self)

    def get_interest_requests(self):
        '''Return all interest requests submitted by this user.'''
        from .models import InterestRequest
        return InterestRequest.objects.filter(requester=self)


class Listing(models.Model):
    '''Represents an apartment or room available for subletting.'''

    lister = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    description = models.TextField(blank=False)
    price_per_month = models.IntegerField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    number_of_roommates = models.IntegerField(blank=True)
    address = models.TextField(blank=False)

    def __str__(self):
        '''Return a readable representation of this listing.'''
        return f'{self.title} – ${self.price_per_month}/month'

    def get_absolute_url(self):
        '''Return URL to display one instance of this listing.'''
        return reverse('listing', kwargs={'pk': self.pk})

    def get_photos(self):
        '''Return all photos associated with this listing.'''
        from .models import ListingPhoto
        return ListingPhoto.objects.filter(listing=self)

    def get_interest_requests(self):
        '''Return all interest requests for this listing.'''
        from .models import InterestRequest
        return InterestRequest.objects.filter(listing=self)


class ListingPhoto(models.Model):
    '''Stores a photo for a Listing.'''

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='listing_photos/', blank=True, null=True)

    def get_image_url(self):
        '''Return file URL'''
        if self.image_file:
            return self.image_file.url
        return self.image_url

    def __str__(self):
        img = self.get_image_url()
        return f"Photo[{img}]" if img else f"Photo id={self.pk}"


class InterestRequest(models.Model):
    '''Represents a user's interest in a specific listing.'''

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    requester = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message_text = models.TextField(blank=False)
    submitted_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        '''representation of an interest request.'''
        return f'{self.requester.display_name} → {self.listing.title} ({self.status})'

    def get_absolute_url(self):
        '''URL to display this request.'''
        return reverse('interestrequest', kwargs={'pk': self.pk})


