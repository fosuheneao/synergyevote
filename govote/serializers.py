from rest_framework import serializers
from .models import Client, Subscription, SubscriptionPlan, SubscriptionPlanChoice, Country, Region, District, City, Area, Title, Designation 

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
    class Meta:
        model = Client
        fields = '__all__'
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'       
                                          
       