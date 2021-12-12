from .models import UserProfileInfo, bodyRegion, cancerTypes, trial, trial_lead

from django.contrib import admin

# Register your models here.
admin.site.register(bodyRegion)
admin.site.register(cancerTypes)
admin.site.register(trial)
admin.site.register(UserProfileInfo)
admin.site.register(trial_lead)

