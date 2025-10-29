from django.shortcuts import render
from django.views.generic import ListView
from .models import Voter

# Create your views here.

class VoterListView (ListView):
    ''' Define a view class to display all voters'''

    model = Voter 
    template_name = "voter_analytics/show_voter.html" 
    context_object_name = "voters"

    def get_queryset(self):
    
        # limit results to first 100 records (for now)
        qs = super().get_queryset()
        return qs[:100] 

