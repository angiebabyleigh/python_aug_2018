from django.conf.urls import url
from apps.word import views           # This line is new!
from django.urls import path

urlpatterns = [
  path('random_word', views.word, name='word'),
  path('random_word/reset', views.reset, name='reset')
]