from .models import UserProfileInfo, bodyRegion, cancerTypes, trial

from django.contrib import admin

# Register your models here.
admin.site.register(bodyRegion)
admin.site.register(cancerTypes)
admin.site.register(trial)
admin.site.register(UserProfileInfo)

