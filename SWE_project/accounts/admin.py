from django.contrib import admin

from .models import Profile, Search_bar_model

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
