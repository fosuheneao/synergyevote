from rest_framework import viewsets, permissions
from .models import Client, Subscription, SubscriptionPlan, SubscriptionPlanChoice,Country, Region, District, City, Area, Title, Designation
from .serializers import ClientSerializer, SubscriptionSerializer, SubscriptionPlanSerializer, SubscriptionPlanChoiceSerializer, CountrySerializer, RegionSerializer, DistrictSerializer, CitySerializer, AreaSerializer, TitleSerializer, DesignationSerializer


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
    
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsSuperUser]  # Only superadmins can modify this

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this
    

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [IsSuperUser]  # Only superadmins can modify this