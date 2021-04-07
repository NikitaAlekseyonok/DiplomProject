from django.urls import path

from .views import *

urlpatterns = [
    path('', headTeacherHomePage, name='headTeacherPage'),
    path('headTeacherPage', studentPage, name='studentPage'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('logout', user_logout, name='logout'),
]
