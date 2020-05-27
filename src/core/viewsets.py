from rest_framework import viewsets, status
from rest_framework.response import Response


class ModelViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        """
        This method will be used by all non-overriden operations
        """
        if self.action in ['create', 'update', 'partial_update']:
            serializer_class = self.get_write_serializer_class()

        # list, retrieve
        serializer_class = self.get_read_serializer_class()

        assert serializer_class is not None
        return serializer_class

    def get_read_serializer_class(self):
        read_serializer_class = getattr(
            self, 'read_serializer_class', None) or super().get_read_serializer_class()
        return read_serializer_class

    def get_write_serializer_class(self):
        write_serializer_class = getattr(
            self, 'write_serializer_class', None) or super().get_read_serializer_class()
        return write_serializer_class

    def get_read_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for serializing output.
        """
        reader_class = self.get_read_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return reader_class(*args, **kwargs)

    def get_write_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input.
        """
        writer_class = self.get_write_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return writer_class(*args, **kwargs)

    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        writer = self.get_write_serializer(data=request.data)
        writer.is_valid(raise_exception=True)
        self.perform_create(writer)
        headers = self.get_success_headers(writer.data)
        reader = self.get_read_serializer(writer.instance)
        return Response(reader.data, status=status.HTTP_201_CREATED, headers=headers)

    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
