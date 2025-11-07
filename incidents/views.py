from rest_framework import generics, pagination, status
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer, IncidentStatusUpdateSerializer
from drf_yasg.utils import swagger_auto_schema
from .swagger_docs import incident_get_schema, incident_post_schema, incident_patch_schema


class IncidentPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    max_limit = 100


class IncidentListView(generics.ListCreateAPIView):
    serializer_class = IncidentSerializer
    pagination_class = IncidentPagination

    def get_queryset(self):
        queryset = Incident.objects.all().order_by('created_at')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @incident_get_schema
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @incident_post_schema
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class IncidentStatusUpdateView(generics.UpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentStatusUpdateSerializer
    lookup_field = 'id'

    @incident_patch_schema
    def patch(self, request, *args, **kwargs):
        if 'status' not in request.data:
            return Response(
                {"status": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        return Response(
            {"detail": "PUT method not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
