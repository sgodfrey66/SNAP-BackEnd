import json
from django.conf import settings
from django.http import HttpResponseNotFound
from django.views import defaults
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from core.logging import logger
import survey.models
import client.models


class HealthViewSet(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        data = {'status': 'up', 'build_version': settings.BUILD_VERSION, 'build_date': settings.BUILD_DATE}
        logger.info('Health check')
        return Response(data)


class UsersMe(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'permissions': str(request.user.user_permissions),
        }
        return Response(content)


class DashboardSummary(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'clients': client.models.Client.objects.for_user(self.request.user).count(),
            'surveys': survey.models.Survey.objects.for_user(self.request.user).count(),
            'responses': survey.models.Response.objects.for_user(self.request.user).count(),
            'questions': survey.models.Question.objects.for_user(self.request.user).count(),
        }
        return Response(content)


def error404(request, exception):
    if request.headers.get('Accept') == 'application/json':
        response_data = {}
        response_data['detail'] = 'Not found.'
        return HttpResponseNotFound(json.dumps(response_data), content_type="application/json")
    return defaults.page_not_found(request, exception)


def error500(request):
    if request.headers.get('Accept') == 'application/json':
        response_data = {}
        response_data['detail'] = 'Internal server error.'
        return HttpResponseNotFound(json.dumps(response_data), content_type="application/json")
    return defaults.server_error(request)
