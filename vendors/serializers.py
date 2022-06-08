from rest_framework import serializers
from .models import Vendor
from django.contrib.auth.models import User

class VendorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','name','products','address','city','pincode','phone','details')
        
class VendorCreateSerializer(serializers.ModelSerializer):
    
    def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        name = data['name']
        products = data['products']
        address = data['address']
        city = data['city']
        pincode = data['pincode']
        phone = data['phone']
        details = data['details']
        todo = Vendor.objects.create(creator=user, name=name, products = products, address=address, city=city,pincode=pincode,phone=phone,details=details)

    class Meta:
        model = Vendor
        fields = ('id','name','products','address','city','pincode','phone','details')

class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
class VendorSpecificListSerializer(serializers.ModelSerializer):
     class Meta:
        model = Vendor
        fields = '__all__'