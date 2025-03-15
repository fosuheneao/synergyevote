from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .api import ClientSerializer, SubscriptionPlanChoiceViewSet, SubscriptionPlanViewSet, SubscriptionViewSet
from . import views

router = DefaultRouter()
router.register(r'subscription-plan-choices', SubscriptionPlanChoiceViewSet)
router.register(r'subscription-plans', SubscriptionPlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'clients', ClientSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path('clients/', views.client_index, name='client'),
    path('api/', include(router.urls)),
]
