from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt
import datetime


# Create your views here.
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data': {"message": "success"}}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Authentication failed, Incorrect username or password'}, status=status.HTTP_401_UNAUTHORIZED)    
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'blablabla', algorithm='HS256') 
        response_data = {'data': {'jwt': token}, 'message': 'success'}
        response = Response(response_data, status=status.HTTP_200_OK)
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response

class UserView(APIView):
    def get(self, request):
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
        
        serializer = UserSerializer(user)
        return Response({'data': serializer.data})

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response