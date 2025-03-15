from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Client, Subscription, SubscriptionPlan, SubscriptionPlanChoice

@admin.register(SubscriptionPlanChoice)
class SubscriptionPlanChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    
    def has_add_permission(self, request):
        #Only superadmins can add new SubscriptionPlanChoice."""
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        #Only superadmins can edit SubscriptionPlanChoice."""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        #Only superadmins can delete SubscriptionPlanChoice."""
        return request.user.is_superuser


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'price', 'duration_days', 'max_voters', 'max_elections')
    search_fields = ('plan_type__name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'plan', 'start_date')
    list_filter = ('plan','client')
    search_fields = ('user__username', 'client__name')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'subdomain', 'location', 'paid_until')
    list_filter = ('name', 'subdomain')
    search_fields = ('name', 'subdomain')
