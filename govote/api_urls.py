from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import * #ClientViewSet, SubscriptionPlanChoiceViewSet, SubscriptionPlanViewSet, SubscriptionViewSet, CountryViewSet

router = DefaultRouter()
router.register(r'subscription-plans-choices', SubscriptionPlanChoiceViewSet)
router.register(r'subscriptions-plans', SubscriptionPlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'clients', ClientViewSet)

router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'cities', CityViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'designations', DesignationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('api/', include(router.urls)),
]
