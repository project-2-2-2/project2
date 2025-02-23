from rest_framework import viewsets, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Customers see only their own requests; support staff see all.
        if user.role == 'customer':
            return ServiceRequest.objects.filter(user=user)
        return ServiceRequest.objects.all()

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the owner
        serializer.save(user=self.request.user)
