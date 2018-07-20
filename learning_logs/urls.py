"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page 
    url(r'^$', views.index, name='index'),

    # Show all medications
    url(r'^medications/$', views.topics, name='medications'),

    # Show information for a single medication
    url(r'^medications/(?P<topic_id>\d+)/$', views.topic, name='medication'),

    # Show information to refill a medication
    url(r'^medications/refills/(?P<zip_code>\d+)/(?P<medication_id>\d+)/$', views.refill, name='refill'),

    # Page for adding new medications
    url(r'^new_medication/$', views.new_topic, name='new_medication'),

    # Page with team member information
    url(r'^support/$', views.support, name='support'),
]