from rest_framework import serializers
from api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'

class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    category = CategorySerializer()
    price = serializers.FloatField()
    description = serializers.CharField()
    ingredients = serializers.CharField()
    images = serializers.CharField()