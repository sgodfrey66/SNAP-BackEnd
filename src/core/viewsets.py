from rest_framework import viewsets


class ModelViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        read_serializer = getattr(
            self, 'read_serializer_class', None) or super().get_serializer_class()
        write_serializer = getattr(
            self, 'write_serializer_class', None) or super().get_serializer_class()

        if self.action in ['create', 'update', 'partial_update']:
            return write_serializer
        return read_serializer
