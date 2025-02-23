from django.urls import path
from .views import AllServiceRequestsView

urlpatterns = [
    path('all-requests/', AllServiceRequestsView.as_view(), name='all_service_requests'),
]
