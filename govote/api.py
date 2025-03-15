from rest_framework import viewsets, permissions
from .models import Client, Subscription, SubscriptionPlan, SubscriptionPlanChoice
from .serializers import ClientSerializer, SubscriptionSerializer, SubscriptionPlanSerializer, SubscriptionPlanChoiceSerializer

class IsSuperUser(permissions.BasePermission):
   # Custom permission to allow only superadmins to create/edit SubscriptionPlanChoice.
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class SubscriptionPlanChoiceViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlanChoice.objects.all()
    serializer_class = SubscriptionPlanChoiceSerializer
    permission_classes = [IsSuperUser]  # Only superadmins can modify this

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]