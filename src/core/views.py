import logging
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import survey.models
import client.models


logger = logging.getLogger('django.server')


class HealthViewSet(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, logger=logging.getLogger('django.server'), format=None):
        logger.error('server error')
        # logging.getLogger('app').debug('app error')
        # logging.getLogger('app').info('app error')
        # logging.getLogger('app').warning('app error')
        # logging.getLogger('app').error('app error')
        # logging.getLogger('app').critical('app error')
        data = {'status': 'up'}
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
