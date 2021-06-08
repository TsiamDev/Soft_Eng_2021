from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.signals import request_started
from django.dispatch import receiver

# Constants
STORE_NAME_LENGTH = 30

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    store_name = models.CharField(max_length=STORE_NAME_LENGTH, unique=True, blank=True)

    # one-to-many: FK
    #favourites = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True, unique=False, default=None)
    # Many-to-many: FKs
    favourites = models.ManyToManyField('Profile')#, on_delete=models.CASCADE, blank=True, null=True, unique=False, default=None)
    #User, on_delete=models.CASCADE)#, related_name='favourites', on_delete=models.CASCADE)

    def __str__(self):
        if self.store_name is not None:
            return self.store_name
        else:
            return self.username

    def get_store_name(self):
        if self.store_name is not None:
            return self.store_name
        else:
            return "Not a store"

"""
class Favourites(models.Model):
    users = Man


    def __str__(self):
"""        
        
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# search stores bar
class Search_bar_model(models.Model):
    search_box = models.CharField(max_length=STORE_NAME_LENGTH, blank=True)
    
    #def __str__(self):
    #    return "search_bar"
"""
@receiver(request_started, sender=Search_bar)
def update_search_reesults(sender, instance, created, **kwargs):
    if created:
        print("created!")
    else:
        print("not created")
"""