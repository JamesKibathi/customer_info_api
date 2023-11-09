from rest_framework import serializers
from .models import Category, Location, Business, Customer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    age_of_business = serializers.ReadOnlyField()

    class Meta:
        model = Business
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
