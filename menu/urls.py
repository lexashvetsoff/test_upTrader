from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('company/', base, {'name': 'About company'}, name='company'),
    path('contacts/', base, {'name': 'Contacts'}, name='contacts'),
    path('work/', base, {'name': 'Work'}, name='work'),
    path('work/cpp', base, {'name': 'Work C++'}, name='work_cpp'),
    path('work/python', base, {'name': 'Work Python'}, name='work_python'),
    path('work/frontend', base, {'name': 'Work frontend'}, name='work_frontend'),
    path('work/frontend/react', base, {'name': 'Work frontend/React'}, name='work_frontend_react'),
    path('work/frontend/angular', base, {'name': 'Work frontend/Angular'}, name='work_frontend_angular'),
    path('prices/', base, {'name': 'Prices'}, name='prices'),
]
