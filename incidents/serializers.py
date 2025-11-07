from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'description', 'status', 'source', 'created_at']
        read_only_fields = ['id', 'created_at']

class IncidentStatusUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=Incident.STATUS_CHOICES,
        required=True,
        help_text="Новый статус инцидента"
    )

    class Meta:
        model = Incident
        fields = ['status']
