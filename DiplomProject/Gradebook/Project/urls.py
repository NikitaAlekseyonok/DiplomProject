from django.urls import path

from .views import *

urlpatterns = [
    path('#', headTeacherHomePage, name='headTeacherHomePage'),
    path('', studentPage, name='studentPage'),
]
