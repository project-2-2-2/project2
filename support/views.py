from rest_framework import generics, permissions
from service_requests.models import ServiceRequest
from service_requests.serializers import ServiceRequestSerializer

class AllServiceRequestsView(generics.ListAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow support staff to view all requests
        if self.request.user.role == 'support':
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.none()
