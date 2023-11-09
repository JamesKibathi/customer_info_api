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
    category = CategorySerializer() 

    class Meta:
        model = Business
        fields = '__all__'
    def create(self, validated_data):
        # Extract the category data from the validated data
        category_data = validated_data.pop('category')
        
        # Create or retrieve the category instance
        category_instance, _ = Category.objects.get_or_create(**category_data)
        
        # Create the business instance
        business_instance = Business.objects.create(category=category_instance, **validated_data)
        
        return business_instance   

class CustomerSerializer(serializers.ModelSerializer):
     # Extract the nested location and business data
    location = LocationSerializer(read_only=True)
    business = BusinessSerializer(read_only=True)

    location_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Location.objects.all(), source='location')
    business_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Business.objects.all(), source='business')
            

    class Meta:
        model = Customer
        fields = '__all__' 
      
        
           

           
            