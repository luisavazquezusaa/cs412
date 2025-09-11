#file: quotes/views.py 

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

# Create your views here.

def home(request):
    '''Define a view to handle the 'home' request.'''
    response_text = '''
    <html>
    <h1>Cardi B Quote Of The Day</h1>
    </html>'''
    
    return HttpResponse(response_text)

def home_page(request): 
    '''Respond to URL', delegate work to a template'''
    template_name = 'quotes/home.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        "letter1": chr(random.randint(65,90),),
        "number": random.randint(1,10), 
        
    }

    return render(request, template_name, context) 

def about(request): 
    '''Respond to URL 'about', delegate work to a template'''
    template_name = 'quotes/about.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        "letter1": chr(random.randint(65,90),),
        "number": random.randint(1,10), 
        
    }

    return render(request, template_name, context) 




