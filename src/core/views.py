from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class HealthViewSet(viewsets.ViewSet):
	permission_classes = (AllowAny, )

	def list(self, request, format=None):
		data = { "status": "up" }
		return Response(data)
