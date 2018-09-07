from django.conf.urls import url
from . import views           # This line is new!
from django.urls import path


urlpatterns = [
  path('', views.start, name='start'),
]