
from django.contrib import admin
from django.urls import path

from BlackFriday import views
from .views import home_view

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('departments/', views.PersonView.as_view()),
]