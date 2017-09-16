#!/usr/bin/env python3

import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj1.settings")
django.setup()

from django.contrib.auth.models import User

if User.objects.all():
    print('Some user already exists')
    sys.exit()

u = User(username='admin')
u.set_password('admin')
u.is_superuser = True
u.is_staff = True
u.save()
