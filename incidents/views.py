from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer


class IncidentListView(generics.ListAPIView):
    serializer_class = IncidentSerializer

    def get_queryset(self):
        queryset = Incident.objects.all().order_by('-created_at')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
