from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from .models import Profile

# Password Reset
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic.edit import CreateView

from django.http import HttpResponse

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
    if request.method == "POST":
        print("regular POST")
        searched = request.POST['search_box']
        try:
            form = StoreSearchForm(request.POST)
        except Exception as e:
            print(e)
    else:
        print("custom POST")
        data = { 'search_box': 'st' }
        searched = data['search_box']
        try:
            form = StoreSearchForm(data)
        except Exception as e:
            print(e)

    if form.is_valid():
        #form.save()
        print("form is valid")
        stores = Profile.objects.filter(store_name__contains=searched)
        context = { 'form' : form, 'stores': stores }
    else:
        print("form is invalid")
        context = { 'form' : form }

    print("got here")
    return render(request, 'search_stores.html', context)#HttpResponse(context)#


class PasswordReset(generic.CreateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_form')
    template_name = 'registration/password_reset_form.html'

def profile_view(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        store = Profile.objects.get(pk=request.user.id)
        #breakpoint()
        context = { 'store_name': store.get_store_name(),
                    'last_login': request.user.last_login,
                    'date_joined': request.user.date_joined,
            }
        return render(request, 'profile.html', context)
    #else:
        # User not authenticated
    
def show_profile_view(request, store_name):
    # store_name is unique
    #store = Profile.objects.get(store_name=store_name)
    store = Profile.objects.get(pk=request.user.id)
    viewed_store = Profile.objects.get(store_name=store_name)
    
    cur_store = Profile.objects.get(user__profile=viewed_store.id)
    print("f: " + str(cur_store.store_name))
    
    if cur_store.store_name == store.store_name:
        print("Same user")
    else:
        print("Different user")
    """
    cur_user = User.objects.get(id=)
    print(cur_user)
    print(request.user)
    if cur_user == request.user:
        print("identical use")
    else:
        print("differrent user")
    """    
    context = { 'store_name': cur_store.get_store_name(),
                'st_username': cur_store.user.username,
                'st_email': cur_store.user.email,
                'st_last_login': cur_store.user.last_login,
                'st_date_joined': cur_store.user.date_joined,
                'st_id': cur_store.id,
        }
    
    return render(request, 'show_profile.html', context)

def favourites_view(request):
    print(request.user)
    user_profile = Profile.objects.get(id=request.user.id)
    print("favs " + str(user_profile.favourites.all()))
    
    favs = {}
    i = 0
    for store in user_profile.favourites.all():
        favs[i] = store.store_name
        print("favs[i]: " + str(favs[i]))
        i = i + 1
    
    context = {
            'favs': favs
        }
    print(user_profile.favourites)
       
    return render(request, 'show_favourites.html', context)
    
def add_to_favourites_view(request, store_id):
    # Get current user profile
    prof = Profile.objects.get(user=request.user)
    #print(prof)
    print(prof.favourites.all())
    
    # Get selected store user profile
    selected = Profile.objects.get(user=store_id)
    #print(selected)
    
    # Save favourite if it does not exist already
    prof.favourites.add(selected)
    
    favs = {}
    i = 0
    for store in prof.favourites.all():
        favs[i] = store.store_name
        print("favs[i]: " + str(favs[i]))
        i = i + 1

    context = { 'favs': favs }
    return render(request, 'show_favourites.html', context)