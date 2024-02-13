from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer, ItemSerializerGet
from rest_framework.permissions import IsAuthenticated
import jwt
from users.models import User

def verify_user(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return Response({'error': 'Unauthenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        payload = jwt.decode(token, 'blablabla', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Unauthenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    user = User.objects.filter(id=payload['id']).first()
    if user is None:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    return True

class CategoryCountView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 

        unique_categories_count = Category.objects.count()
        response = Response({
            'data': {'categories_count': unique_categories_count},
        }, status=status.HTTP_200_OK)
        return response

class ItemCountView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 
     
        unique_items_count = Item.objects.count()
        response = Response({
            'data': {'items_count': unique_items_count},
        }, status=status.HTTP_200_OK)
        return response

class CategoryCreateView(CreateAPIView):
    def post (self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 
        
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class ItemCreateView(CreateAPIView):
    def post(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 
    
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
            return Response({"data": {"message": "success"}}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CategoryListView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 
    
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class ItemListView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 
    
        items = Item.objects.all()
        serializer = ItemSerializerGet(items, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class CategoryFilterView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 

        name = request.query_params.get('name', None)
        if name:
            categories = Category.objects.filter(name__icontains=name)
            if categories.exists():
                return Response({'data' : {"exists": True}})
            else:
                return Response({'data': {"exists": False}})
        else:
            return Response({"error": "No category name provided"}, status=400)


class ItemFilterView(APIView):
    def get(self, request):
        verification = verify_user(request)
        if verification != True:
            return verification 

        sku = request.query_params.get('sku', None)
        name = request.query_params.get('name', None)
        tags = request.query_params.get('tags', None)
        category = request.query_params.get('category', None)
        in_stock = request.query_params.get('in_stock', None)
        available = request.query_params.get('available', None)

        items = Item.objects.all()

        if sku:
            items = items.filter(sku__icontains=sku)
        if name:
            items = items.filter(name__icontains=name)
        if tags:
            items = items.filter(tags__icontains=tags)
        if category:
            items = items.filter(category__name__icontains=category)
        if in_stock:
            items = items.filter(in_stock__icontains=in_stock)
        if available:
            items = items.filter(available__icontains=available)

        serializer = ItemSerializer(items, many=True)
        return Response({'data': serializer.data})
