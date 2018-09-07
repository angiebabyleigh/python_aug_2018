from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
  path('session_word', views.words, name='words'),
  path('session_word/clear', views.clear, name='clear')
]