# Generated by Django 3.0.8 on 2020-07-20 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0012_remove_agency_programs'),
        ('program', '0008_auto_20200717_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='agency.Agency'),
        ),
        migrations.DeleteModel(
            name='AgencyProgramConfig',
        ),
    ]
