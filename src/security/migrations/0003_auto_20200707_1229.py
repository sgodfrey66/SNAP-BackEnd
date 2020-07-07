# Generated by Django 3.0.7 on 2020-07-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20200707_1229'),
        ('security', '0002_auto_20200707_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='securitygroup',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='securitygroup',
            name='agencies',
            field=models.ManyToManyField(related_name='security_groups', to='agency.Agency'),
        ),
        migrations.AlterField(
            model_name='securitygroup',
            name='enrollments',
            field=models.BooleanField(default=False, verbose_name='Access Client enrollment data'),
        ),
        migrations.AlterField(
            model_name='securitygroup',
            name='referrals',
            field=models.BooleanField(default=False, verbose_name='Access Client referral data'),
        ),
        migrations.AlterField(
            model_name='securitygroup',
            name='responses',
            field=models.BooleanField(default=False, help_text='Grants access to responses created by any of the agencies within the security group', verbose_name='Access Responses'),
        ),
    ]
