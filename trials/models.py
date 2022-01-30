from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    # additional classes
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class bodyRegion(models.Model):
    body_region = models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.body_region}")

class cancerTypes(models.Model):    
    cancer_type = models.CharField(max_length=200)
    body_region = models.ForeignKey(bodyRegion, on_delete=models.CASCADE, null=True) 

    class Meta:
        verbose_name = 'cancerType'
        verbose_name_plural = 'cancerTypes'

    def __str__(self):
        return (f"{self.body_region} {self.cancer_type}")

    def get_absolute_url(self):
        return reverse('trials:cancerTypes')

class trial_lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.last_name}")

    def get_absolute_url(self):
        return reverse('trials:trial_lead')

class trial(models.Model):    
    name = models.TextField()
    description = models.TextField()
    end_date = models.DateField(null=False)
    inclusion_criteria = models.TextField()
    exclusion_criteria = models.TextField()
    body_region = models.ForeignKey(bodyRegion, on_delete=models.CASCADE)
    cancer_type = models.ForeignKey(cancerTypes, on_delete=models.CASCADE)
    trial_lead = models.ForeignKey(trial_lead, on_delete=models.CASCADE, null=True)    
    Trial_ended = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.name}")

