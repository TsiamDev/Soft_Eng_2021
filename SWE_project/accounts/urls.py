# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:41:22 2021

@author: Perhaps
"""

from django.urls import path

#from .views import SignUpView, PasswordReset
from .views import PasswordReset
from .views import *


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', signup, name='signup'),
    path('store_signup/', store_signup, name='store_signup'),
    #path('search_stores/', SearchBar.as_view(), name='search_stores'),
    path('search_stores/', search_stores_view, name='search_stores'),
    path('profile/', profile_view, name='profile'),
    path('ckeck_availability/<store_name>', check_availability_view, name='check_availability'),
    path('make_appointment/<store_name>', make_appointment_view, name='make_appointment'),
    path('show_profile/<store_name>', show_profile_view, name='show_profile'),
    path('favourites/', favourites_view, name='favourites'),
    path('add_to_favourites/<store_id>', add_to_favourites_view, name='add_to_favourites'),
    #path('signup/', home_view, name='signup'),
    path('password_reset_form/', PasswordReset.as_view(), name='password_reset_form'),
]