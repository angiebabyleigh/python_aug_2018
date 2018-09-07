from django.conf.urls import url
from apps.survey import views
from django.urls import path

urlpatterns = [
    path('', views.survey, name='survey'),
]