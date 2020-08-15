# Generated by Django 3.0.8 on 2020-08-15 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
                ('name', models.CharField(max_length=64)),
                ('ref_id', models.IntegerField(null=True, unique=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Agencies',
                'db_table': 'agency',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AgencyClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=125, null=True)),
                ('agency_ref', models.ForeignKey(db_column='agency_ref', null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency', to_field='ref_id')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agency_clients', to='client.Client')),
            ],
            options={
                'db_table': 'agency_client',
            },
        ),
    ]
