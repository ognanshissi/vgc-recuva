import datetime
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Group, GroupZone
from .serializers import ZoneSerializer
from rest_framework import status


class GroupZoneCreateAPIView(APIView):

    def get(self, request, pk, format=None):
        _id = self.kwargs.get('pk')
        g = get_object_or_404(Group, pk=_id)
        zones = GroupZone.objects.filter(group=g)
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        data = request.POST
        name = data.get('name', None)
        qs = GroupZone.objects.filter(name__iexact=name).exists()

        if qs:
            data = {
                'success': False,
                'message': 'Une erreur est survenue',
                'error_messages': {
                    'name': 'la zone existe deja '
                }
            }
        else:
            g = get_object_or_404(Group, pk=data.get('group_id'))
            GroupZone.objects.create(name=name, group=g)
            data = {
                'success': True,
                'message': 'La zone a bien été enregisté',

            }
        return Response(data)
        # serializer = ZoneSerializer(data=request.POST)
        # if serializer.is_valid():
        #     g = get_object_or_404(Group, pk=pk)
        #     instance = serializer.save(commit=False)
        #     instance.group = g
        #     instance.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

