# Generated by Django 3.0.7 on 2020-07-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20200521_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-created_at']},
        ),
    ]
