from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    #is_store = forms.BooleanField(help_text='Required')

    class Meta:
        model = User
        fields = ('email', 'username', 'birth_date', 'password1', 'password2', 'is_active')

class StoreSignUpForm(UserCreationForm):
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    #is_store = forms.BooleanField(help_text='Required')
    store_name = forms.CharField(help_text='Required. This is your store\'s name.', required=True)
    
    class Meta:
        model = User
        fields = ('store_name', 'email', 'username', 'password1', 'password2', )

class StoreSearchForm(forms.ModelForm):
    search_box = forms.CharField(help_text='Input the store name here.', label='searched')
    
    class Meta:
        model = Search_bar_model
        fields = ['search_box', ]
        