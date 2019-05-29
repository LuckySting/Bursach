# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0713671/data/www/luckysting.space/bursach/SocialHouse')
sys.path.insert(1, '/var/www/u0713671/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'SocialHouse.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()