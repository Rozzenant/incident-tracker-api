from django.urls import path
from .views import IncidentListView, IncidentStatusUpdateView

urlpatterns = [
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    path(
        'incidents/<int:id>/',
        IncidentStatusUpdateView.as_view(),
        name='incident-update-status',
    ),
]
