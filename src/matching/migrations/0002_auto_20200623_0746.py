# Generated by Django 3.0.7 on 2020-06-23 07:46

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientmatching',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='clientmatchinghistory',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='clientmatchingnote',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='clientmatchinghistory',
            name='created_at',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='clientmatchinghistory',
            name='modified_at',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at'),
        ),
        migrations.AddField(
            model_name='clientmatchingnote',
            name='created_at',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='clientmatchingnote',
            name='modified_at',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at'),
        ),
    ]
