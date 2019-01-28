from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Profile
from datetime import datetime
from collections import defaultdict 
#
# Create your views here.

def profile(request, username):
    user = Profile.objects.get(user__username = username)
    user.name = user.user.get_full_name()
    user.sname = user.user.get_short_name()
    user.email = user.user.email
    return render(request, "alumniprofile/profile.html", vars(user))

def index(request):
    years = set(Profile.objects.all().values_list('batch', flat=True)) 
    print(years)    
    return render(request, "alumniprofile/index.html", {'years':years})

def index_year(request, year):
    alumni = Profile.objects.filter(batch = year)
    return render(request, "alumniprofile/index_year.html", {'alumni':alumni})


