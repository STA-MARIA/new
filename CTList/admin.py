from django.contrib import admin
from .models import *

admin.site.register([User, Subscription, Feedback, Guides, Feeds])
# Register your models here.
