from django.utils.module_loading import import_string
from rest_framework import serializers


class ContentObjectRelatedField(serializers.RelatedField):
    """
    A custom field to serialize generic relations
    """

    def to_representation(self, object):
        object_app = object._meta.app_label
        object_name = object._meta.object_name
        serializer_module_path = f'{object_app}.serializers.{object_name}Reader'
        serializer_class = import_string(serializer_module_path)
        data = serializer_class(object).data
        return data


class ObjectSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()

    def get_object(self, object):
        return object._meta.object_name
