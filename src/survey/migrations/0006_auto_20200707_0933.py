# Generated by Django 3.0.7 on 2020-07-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20200605_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['-created_at']},
        ),
    ]
