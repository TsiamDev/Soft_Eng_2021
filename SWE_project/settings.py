"""
Django settings for SWE_project project.

(re)place the following to the settings file
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'path//to//my.cnf',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}


STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join('sent_emails')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
