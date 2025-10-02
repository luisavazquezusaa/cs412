from django.contrib import admin

# Register your models here.
#from .models import Article from example, commented it out
#admin.site.register(Article)

from .models import Profile, Post, Photo #Comment #registering the comment 
admin.site.register(Profile)
# admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Photo)
