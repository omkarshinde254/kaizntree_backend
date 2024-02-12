from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'tags', 'category', 'in_stock', 'available']
