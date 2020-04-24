# Generated by Django 3.0.5 on 2020-04-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('survey', '0002_auto_20200422_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='public',
        ),
        migrations.RemoveField(
            model_name='response',
            name='client',
        ),
        migrations.AddField(
            model_name='question',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='respondent_id',
            field=models.UUIDField(default='00000000-0000-0000-0000-000000000000'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='respondent_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='responses', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='other',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='refusable',
            field=models.BooleanField(default=False),
        ),
    ]
