from django.contrib import admin
from .models import (ContactProfile, PatientProfile)

admin.site.register(ContactProfile)
admin.site.register(PatientProfile)