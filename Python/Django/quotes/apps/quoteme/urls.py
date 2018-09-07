from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.login, name='login'),
  path('register',views.register, name='register'),
  path('myaccount/<user_num>', views.edit, name='edit'),
  path('quotes', views.quotes, name='quotes'),
  path('add', views.addquote, name='addquote'),
  path('user/<user_num>', views.userquotes, name='userquotes'),
  path('like', views.like, name='like'),
  path('myaccount/update', views.update, name='update'),
]