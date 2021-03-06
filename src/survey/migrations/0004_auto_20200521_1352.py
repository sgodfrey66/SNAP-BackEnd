# Generated by Django 3.0.5 on 2020-05-21 13:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200424_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, null=True, size=None),
        ),
    ]
