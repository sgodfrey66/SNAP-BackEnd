# Generated by Django 3.0.7 on 2020-07-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eligibility', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agencyeligibilityconfig',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='clienteligibility',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='eligibility',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Eligibility'},
        ),
    ]