# Generated by Django 3.2.5 on 2021-10-20 19:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0004_userprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
