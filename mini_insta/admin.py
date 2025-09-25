from django.contrib import admin

# Register your models here.
#from .models import Article from example, commented it out
#admin.site.register(Article)

from .models import Profile
admin.site.register(Profile)
