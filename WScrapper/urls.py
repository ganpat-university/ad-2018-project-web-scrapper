from django.urls import path
from . import views

urlpatterns ={
	path('',views.index,name='index'),
	path('outcome',views.outcome,name='outcome')
}