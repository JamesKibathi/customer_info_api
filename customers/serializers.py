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
    
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), source='category')
    
    class Meta:
        model = Business
        fields = '__all__'
        
    def to_representation(self, instance):
        # Serialize the associated category details
        category_serializer = CategorySerializer(instance.category)
        category_data = category_serializer.data

        # Calculate the age_of_business
        age_of_business = instance.age_of_business

        # Combine the serialized data into the response
        representation = super(BusinessSerializer, self).to_representation(instance)
        representation['category'] = category_data
        representation['age_of_business'] = age_of_business

        return representation

class CustomerSerializer(serializers.ModelSerializer):
     # Extract the nested location and business data
    location = LocationSerializer(read_only=True)
    business = BusinessSerializer(read_only=True)

    location_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Location.objects.all(), source='location')
    business_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Business.objects.all(), source='business')
            

    class Meta:
        model = Customer
        fields = '__all__' 
      
        
           

           
            