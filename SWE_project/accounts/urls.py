# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:41:22 2021

@author: Perhaps
"""

from django.urls import path

from .views import SignUpView, PasswordReset


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset_form/', PasswordReset.as_view(), name='password_reset_form'),
]