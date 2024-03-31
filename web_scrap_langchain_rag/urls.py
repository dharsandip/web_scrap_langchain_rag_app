from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_query, name = 'process_query'),
]