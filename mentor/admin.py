from django.contrib import admin
from .models import Patch, Instance, Attempt

admin.site.register(Patch)
admin.site.register(Instance)
admin.site.register(Attempt)
