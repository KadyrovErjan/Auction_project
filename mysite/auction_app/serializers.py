from rest_framework import serializers
from .models import *

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name']


class CarModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['car_model']

class CarListSerializers(serializers.ModelSerializer):
    car_brand = BrandSerializers()
    car_model = CarModelSerializers()
    seller = UserProfileSerializers()
    class Meta:
        model = Car
        fields = ['car_brand', 'car_model', 'year', 'price']


class AuctionSerializers(serializers.ModelSerializer):
    car = CarListSerializers()
    class Meta:
        model = Auction
        fields = ['car', 'start_price', 'min_price', 'start_time', 'end_time', 'status']

class BidSerializers(serializers.ModelSerializer):
    auction = AuctionSerializers()
    buyer = UserProfileSerializers()
    class Meta:
        model = Bid
        fields = ['auction', 'buyer', 'amount', 'created_at']

class FeedbackSerializers(serializers.ModelSerializer):
    seller = UserProfileSerializers()
    buyer = UserProfileSerializers()
    class Meta:
        model = Feedback
        fields = ['seller', 'buyer', 'rating', 'comment', 'created_at']

class BrandDetailSerializers(serializers.ModelSerializer):
    car = CarListSerializers(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['brand_name', 'car_brand']

class CarModelDetailSerializers(serializers.ModelSerializer):
    car = CarListSerializers(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['brand_name', 'car_brand']


class CarDetailSerializers(serializers.ModelSerializer):
    car_brand = BrandSerializers()
    car_model = CarModelSerializers()
    seller = UserProfileSerializers()
    class Meta:
        model = Car
        fields = ['car_brand', 'car_model', 'year', 'car_image''fuel_type', 'transmission', 'mileage', 'price', 'description']
