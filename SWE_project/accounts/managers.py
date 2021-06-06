from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

from SWE_project import settings
"""
class CustomUserManager(BaseUserManager):
    
    #Custom user model manager where email is the unique identifiers
    #for authentication instead of usernames.
    
    def create_user(self, email, password, **extra_fields):
        
        #Create and save a User with the given email and password.
        
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The username must be set'))
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            **extra_fields
        )
        
        if validate_password(password, user, settings.AUTH_PASSWORD_VALIDATORS) is None:
            raise ValidationError('password validation error')
        else:
            user.set_password(password)

        #user = self.model(email=email, **extra_fields)
        #if check_password(password):
        #user.set_password(password)
        #else:
        #    raise ValidationError('pwd validation error')
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        #Create and save a SuperUser with the given email and password.
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

"""