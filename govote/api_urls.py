from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ClientViewSet, SubscriptionPlanChoiceViewSet, SubscriptionPlanViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'subscription-plans-choices', SubscriptionPlanChoiceViewSet)
router.register(r'subscriptions-plans', SubscriptionPlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('api/', include(router.urls)),
]
