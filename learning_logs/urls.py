"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page 
    url(r'^$', views.index, name='index'),

    # Show all topics
    url(r'^medications/$', views.topics, name='medications'),

    # Page for adding new topics
    url(r'^new_medication/$', views.new_topic, name='new_medication'),
]