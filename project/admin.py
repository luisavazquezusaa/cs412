from django.contrib import admin
from .models import UserProfile, Listing, ListingPhoto, InterestRequest

admin.site.register(UserProfile)
admin.site.register(Listing)
admin.site.register(ListingPhoto)
admin.site.register(InterestRequest)
