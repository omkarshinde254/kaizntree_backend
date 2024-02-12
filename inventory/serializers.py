from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    sku = serializers.CharField()
    name = serializers.CharField()
    tags = serializers.CharField()
    category = serializers.CharField(source='category.name')
    inStock = serializers.CharField(source='in_stock')
    availableStock = serializers.CharField(source='available')

    class Meta:
        model = Item
        fields = ['id', 'sku', 'name', 'tags', 'category', 'inStock', 'availableStock']