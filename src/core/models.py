from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import UUIDModel, SoftDeletableModel, AutoCreatedField, AutoLastModifiedField
from django.db.models.signals import post_save
from django.dispatch import receiver


class PrimaryModel(UUIDModel, SoftDeletableModel):
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    created_at = AutoCreatedField(_('created_at'))
    modified_at = AutoLastModifiedField(_('modified_at'))

    class Meta:
        abstract = True


class UserProfile(models.Model):
    class Meta:
        db_table = 'user_profile'
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    agency = models.ForeignKey(
        'agency.Agency', related_name='user_profiles', on_delete=models.PROTECT, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
