# Generated by Django 3.0.8 on 2020-07-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0011_remove_agency_is_removed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='programs',
        ),
    ]
