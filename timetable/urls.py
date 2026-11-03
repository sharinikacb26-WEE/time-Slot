from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
]