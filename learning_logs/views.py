from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic
from .forms import TopicForm

from learning_logs import secrets

import googlemaps
import random

# Create your views here.
def index(request):
    """The home page for Silver Fix"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all medications."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics }
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single medication and all its entries"""
    medication = get_object_or_404(Topic, id=topic_id)
    
    # Make sure the topic belongs to the current user.
    if medication.owner != request.user:
        raise Http404

    context = {'medication': medication}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:medications'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def refill(request, medication_id):
    """Show refill options for a specific medication"""
    medication = get_object_or_404(Topic, id=medication_id)

    # Make sure the topic belongs to the current user.
    if medication.owner != request.user:
        raise Http404

    def get_price(id, orig_price):
        random.seed(id)

        buffer = orig_price*0.2
        return random.uniform(orig_price-buffer, orig_price+buffer)

    def show_pharmacies():
        gmaps = googlemaps.Client(key=secrets.GOOGLE_API)
        geocode_result = gmaps.geocode('64108')
        coords = geocode_result[0]['geometry']['location']
        pharmacies_results = gmaps.places(query='', location=coords, type='pharmacy', radius=5)['results']

        for pharmacy in pharmacies_results:
            pharmacy['price'] = get_price(pharmacy['id'], medication.price)

        return sorted(pharmacies_results, key=lambda k: k['price'])

    context = {'medication': medication, 'pharmacies': show_pharmacies()}
    return render(request, 'learning_logs/refill.html', context)

def support(request):
    """ The support page for Silver Fix """
    return render(request, 'learning_logs/support.html')