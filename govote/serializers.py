from rest_framework import serializers
from .models import Client, Subscription, SubscriptionPlan, SubscriptionPlanChoice

class SubscriptionPlanChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlanChoice
        fields = '__all__'

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    plan_type = SubscriptionPlanChoiceSerializer(read_only=True)

    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    #plan = SubscriptionPlanSerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'