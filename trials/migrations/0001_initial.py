# Generated by Django 3.2.5 on 2021-10-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bodyRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_region', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cancerTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancer_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('end_date', models.DateField()),
                ('inclusion_criteria', models.CharField(max_length=200)),
                ('exclusion_criteria', models.CharField(max_length=200)),
                ('body_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trials.bodyregion')),
                ('cancer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trials.cancertypes')),
            ],
        ),
    ]
