import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'SocialHouse.settings'
django.setup()



from django.contrib.auth.models import User
users = list(User.objects.all())
a = 1