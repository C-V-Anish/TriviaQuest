from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,User,MyTokenObtainPairSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LoginView(GenericAPIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username,password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            serializer = UserSerializer(user)

            return Response({
                'access_token': access_token,
                'user': serializer.data,
            },status.HTTP_200_OK)
        
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        