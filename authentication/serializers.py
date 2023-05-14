from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=6,max_length=20)
    last_name = serializers.CharField(min_length=6,max_length=20)
    username = serializers.CharField(min_length=8)
    password = serializers.CharField(min_length=10,write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self,attrs):
        username = attrs.get('username','')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'message':'Username already in use'})
        return super().validate(attrs)
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(min_length=12,max_length=32)
    password=serializers.CharField(min_length=8,write_only=True)
    class Meta:
        model=User
        fields=['username','password']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)