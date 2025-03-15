from django.db import models
from django.utils import timezone
from django_tenants.models import TenantMixin, DomainMixin
# Create your models here.
#############################################################################################
############################ MULTI TENANT SETUP ###################################
# 
# Multi-Tenancy Setup
class Client(TenantMixin):
    name = models.CharField(max_length=500)
    description = models.TextField(default="", null=True, blank=True)
    subdomain = models.CharField(max_length=50, unique=True)  # Ensure unique subdomain
    location = models.CharField(max_length=255, default="", blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='client/photos/', null=True, blank=True, verbose_name="Attach Photo")
    paid_until = models.DateField(default=timezone.now)
    on_trial = models.BooleanField(default=False)
    schema_name = models.CharField(max_length=100, unique=True)  # Schema must be unique
    created_on = models.DateTimeField(default=timezone.now)  # Automatically set timestamp

    class Meta:
        ordering = ['-created_on']  # Sort clients by newest first

    def __str__(self):
        return f"{self.name} ({self.location})"

class Domain(DomainMixin):
    tenant = models.OneToOneField('govote.Client', on_delete=models.CASCADE,related_name="domains")



class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    flag = models.ImageField(upload_to='country/flag/', null=True, blank=True, verbose_name="Attach Country Flag") 
    description = models.TextField(default="")   
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_countries')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Country'
        
    def __str__(self):
        return self.name 
    
# Model for Region linked to Country
class Region(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)  # ISO country code, e.g., "GR" for Greater Accra
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(default="")
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant  
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_regions')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Regions'
        
    def __str__(self):
        return self.name 
    
# Model for District linked to Region
class District(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(default="") 
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant  
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_districts')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Districts'
        
    def __str__(self):
        return self.name 
    
# Model for City linked to District
class City(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="")
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(default="")  
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_cities')
    created_at = models.DateTimeField(default=timezone.now)
        
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'City'
        
    def __str__(self):
        return self.name 
    
# Model for City linked to District
class Title(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="")
    description = models.TextField(default="")   
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_titles')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Titles'
        
    def __str__(self):
        return self.name 
    
# Model for City linked to District
class Designation(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="")
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant
    description = models.TextField(default="")    
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_designations')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Designations'
        
    def __str__(self):
        return self.name 
    
# Model for District linked to Region
class Area(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default="")
    client  = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Link to tenant
    description = models.TextField(default="")    
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_areas')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Areas'
        
    def __str__(self):
        return self.name 

class SubscriptionPlanChoice(models.Model):
    #Defines types of subscription plans that only superadmins can create.   
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default="")
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_subscription_planchoice')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Subscription Plan Choices"

    def __str__(self):
        return self.name


class SubscriptionPlan(models.Model):
    #Subscription plans that users can subscribe to. These reference SubscriptionPlanChoice.
    plan_type = models.ForeignKey(SubscriptionPlanChoice, on_delete=models.PROTECT, related_name="plans")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration_days = models.PositiveIntegerField(default=30)  # Default duration in days
    max_voters = models.PositiveIntegerField(default=0)  # Limit number of voters
    max_elections = models.PositiveIntegerField(default=0)  # Limit number of elections
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_subscriptionplan')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['price']
        verbose_name_plural = "Subscription Plans"

    def __str__(self):
        return f"{self.plan_type.name} - ${self.price}"


class Subscription(models.Model):
    #Manages user subscriptions to a particular tenant with an assigned plan.
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Link to tenant
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)  # Reference SubscriptionPlan
    start_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_subscriptions')
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def is_active(self):
        return self.end_date is None or self.end_date >= timezone.now().date()

    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Subscriptions"

    def save(self, *args, **kwargs):
        #Automatically set the `end_date` based on the plan's duration if not provided."""
        if not self.end_date:
            self.end_date = self.start_date + timezone.timedelta(days=self.plan.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username } - {self.plan.plan_type.name} ({'Active' if self.is_active else 'Expired'})"


# class SubscriptionPlan(models.Model):
#     #Defines types of subscription plans that only superadmins can create.
#     name = models.CharField(max_length=50, unique=True)
#     description = models.TextField(blank=True, default="")
#     duration_days = models.PositiveIntegerField(default=30)  # Default duration in days
#     max_voters = models.PositiveIntegerField(default=0)  # Limit number of voters
#     max_elections = models.PositiveIntegerField(default=0)  # Limit number of elections
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     created_at = models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering = ['name']
#         verbose_name_plural = "Subscription Plans"

#     def __str__(self):
#         return self.name
    
# class Subscription(models.Model):
#     user = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name='created_subscription')
#     client  = models.ForeignKey(Client, on_delete=models.CASCADE)  # Link to tenant
#     plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT, related_name="plans")
#     start_date = models.DateField(default=timezone.now)
#     end_date = models.DateField(null=True, blank=True)
    
#     @property
#     def is_active(self):
#         return self.end_date is None or self.end_date >= timezone.now().date()

#     class Meta:
#         ordering = ['-start_date']
#         verbose_name_plural = "Subscriptions"

#     def save(self, *args, **kwargs):
#         #Automatically set the `end_date` based on the plan's duration if not provided."""
#         if not self.end_date:
#             self.end_date = self.start_date + timezone.timedelta(days=self.plan.duration_days)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.client.name} - {self.plan.name} ({'Active' if self.is_active else 'Expired'})"
