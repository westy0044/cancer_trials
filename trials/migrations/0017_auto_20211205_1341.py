# Generated by Django 3.2.5 on 2021-12-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0016_trial_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial_lead',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trial_lead',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
