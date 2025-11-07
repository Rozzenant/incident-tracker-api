from rest_framework import generics, pagination
from .models import Incident
from .serializers import IncidentSerializer


class IncidentPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    max_limit = 100


class IncidentListView(generics.ListAPIView):
    serializer_class = IncidentSerializer
    pagination_class = IncidentPagination

    def get_queryset(self):
        queryset = Incident.objects.all().order_by('-created_at')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

