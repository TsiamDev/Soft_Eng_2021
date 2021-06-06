from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *

# Password Reset
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic.edit import CreateView

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def store_signup(request):
    if request.method == 'POST':
        form = StoreSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.store_name = form.cleaned_data.get('store_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = StoreSignUpForm()
    return render(request, 'registration/store_signup.html', {'form': form})

def home(request):
    if request.method == 'POST':
        form = StoreSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.store_name = form.cleaned_data.get('store_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = StoreSignUpForm()
    return render(request, 'registration/store_signup.html', {'form': form})

def search_stores_view(request):
    breakpoint()
    
    if request.method == "POST":
        print("regular POST")
        form = StoreSearchForm(request.POST)
    else:
        print("custom POST")
        data = { 'search_box': 'aaa' }
        form = StoreSearchForm(initial=data)
    if form.is_valid():
        #form.save()
        print("form is valid")
        context = {
            'form' : form
        }
    else:
        print("empty contrext")
        context = {}
    
    return render(request, 'search_stores.html', context)
    """
    if request.method == "POST":
        send = { 'val': 'sent!' } 
        return render(request, 'search_stores.html', {'send': send})
    else:
        return render(request, 'search_stores.html', {})
    """
"""
class SearchBar(CreateView):
    model = StoreSearchForm#Search_bar
    fields = ['search_box']
    #form_class = StoreSearchForm
    #success_url = reverse_lazy('search_stores.html')
    #template_name = 'search_stores.html'
    def search_stores(request):
        print("here")
        if request.method == 'POST':
            print("is post")
            form = StoreSearchForm(request.POST or None)
            #if form.is_valid():
            print(" is valid")
            searched = request.POST.get('searched', 0)
            print("searched: " + str(searched))
            return render(request, 'search_stores.html', {'searched': searched})
            #else: 
            #    print("is not valid")
            #    return render(request, 'search_stores.html', {})    
        else:
            print("not post")
            return render(request, 'search_stores.html', {})
"""
class PasswordReset(generic.CreateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_form')
    template_name = 'registration/password_reset_form.html'


"""
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic

#from .forms import CustomUserForm
from .models import Profile
#from django.shortcuts import render

class SignUpView(generic.CreateView):
    #form_class = UserCreationForm
    #form_class = CustomUserForm
    form_class = Profile
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class PasswordReset(generic.CreateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_form')
    template_name = 'registration/password_reset_form.html'
"""
"""    
def home_view(request):
    context ={}
  
    # create object of form
    form = CustomUserForm(request.POST or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "home.html", context)
"""