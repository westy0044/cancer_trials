# Generated by Django 3.2.5 on 2021-11-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0013_trial_trial_ended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
