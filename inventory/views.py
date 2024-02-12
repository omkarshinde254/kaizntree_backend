from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryCountView(APIView):
    def get(self, request):
        unique_categories_count = Category.objects.count()
        response = Response({
            'categories_count': unique_categories_count,
        }, status=status.HTTP_200_OK)
        return response

class ItemCountView(APIView):
    def get(self, request):
        unique_items_count = Item.objects.count()
        response = Response({
            'items_count': unique_items_count,
        }, status=status.HTTP_200_OK)
        return response

class CategoryCreateView(CreateAPIView):
    def post (self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemCreateView(CreateAPIView):
    def post(self, request):
        category_name = request.data.get('category')
        sku = request.data.get('sku')

        if Item.objects.filter(sku=sku).exists():
            return Response({"error": "Item with this SKU already exists"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        request.data['category'] = category.id
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)