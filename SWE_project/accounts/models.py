from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.signals import request_started
from django.dispatch import receiver
from django.utils import timezone

# Constants
STORE_NAME_LENGTH = 30

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    store_name = models.CharField(max_length=STORE_NAME_LENGTH, unique=True, blank=True, null=True, default=None)

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
    
class Make_appointment_model(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)#, default=None)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    #appointment_list = models.ManyToManyField(Profile)#, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        print("self.id: " + str(self.id))
        if self.id is None:
            if Make_appointment_model.objects.all().exists():
                i = Make_appointment_model.objects.all().order_by('-id')[0]
                self.id = i.id+1
            else:
                self.id = 1
            print("new id: " + str(self.id))
        super(Make_appointment_model, self).save(*args, **kwargs) 

"""
@receiver(request_started, sender=Search_bar)
def update_search_reesults(sender, instance, created, **kwargs):
    if created:
        print("created!")
    else:
        print("not created")
"""