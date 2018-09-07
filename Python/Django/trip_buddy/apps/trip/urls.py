from django.conf.urls import url
from . import views           # This line is new!
from django.urls import path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('register',views.register, name='register'),
  path('dashboard', views.maintravels, name='travels'),
  path('add', views.add, name='add'),
  path('addTrip', views.addTrip, name="addTrip"),
  path('view/<trip_num>', views.viewTrip, name="viewTrip"),
  path('join/<trip_num>', views.joinTrip, name="joinTrip"),
  path('delete/<trip_num>', views.deleteTrip, name="deleteTrip"),
  path('cancel/<trip_num>/<user_num>', views.cancelTrip, name="cancelTrip"),
]
