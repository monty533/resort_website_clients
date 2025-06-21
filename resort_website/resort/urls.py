from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('facilities/', facilities_view, name='facilities'),
    path('room/', room_view, name='room'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('banquet/', banquet_view, name='banquet'),
    path('contact/', contact_view, name='contact'),
    path('term_condition/', term_condition_view, name='term_condition'),
    
]