from rest_framework import generics, pagination
from .models import Incident
from .serializers import IncidentSerializer
from drf_yasg.utils import swagger_auto_schema
from .swagger_docs import incident_get_schema, incident_post_schema


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
