# Generated by Django 3.2.5 on 2021-10-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0005_alter_userprofileinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
