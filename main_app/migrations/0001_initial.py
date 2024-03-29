# Generated by Django 4.2.11 on 2024-03-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_names', models.CharField(max_length=100)),
                ('botanical_name', models.CharField(max_length=100)),
                ('light_need', models.TextField(max_length=250)),
                ('water_need', models.TextField(max_length=250)),
                ('soil_type', models.TextField(max_length=250)),
                ('leaf_description', models.TextField(max_length=250)),
                ('toxic', models.BooleanField(default=True)),
                ('native_to', models.TextField(max_length=250)),
                ('acquired_via', models.TextField(max_length=250)),
            ],
        ),
    ]
