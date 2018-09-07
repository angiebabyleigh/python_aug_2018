from django.conf.urls import url
from . import views           # This line is new!
from django.urls import path
urlpatterns = [

	path('', views.index),
	path('new', views.new),
	path('create', views.create),
	path('<int:number>', views.show),
	path('<int:number>/edit', views.edit),
	path('<int:number>/delete', views.destroy),

]                            


