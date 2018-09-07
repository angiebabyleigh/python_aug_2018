from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('dashboard', views.mainjobs, name='jobs'),
  path('addJob', views.addjob, name='addjob'),
  path('add', views.add, name='add'),
  path('view/<job_num>', views.viewjob, name='view'),
  path('edit/<job_num>', views.edit, name='edit'),
  path('delete/<job_num>', views.deletejob, name='cancel'),
  path('accept/<job_num>', views.acceptjob, name='accept'),
  path('complete/<job_num>', views.completejob, name='complete'),
]