from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=15, min_length=6)
    password = serializers.CharField(max_length=20, min_length=6)
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username is already taken.')
        if len(value) < 6 or len(value) > 15:
            raise serializers.ValidationError('Username be between 6 to 15 characters')
        return value
    
    def validate_password(self, value):
        if len(value) < 6 or len(value) > 20:
            raise serializers.ValidationError('Password be between 6 to 15 characters')
        return value

    # Optional: If you want to customize the behavior for saving the password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
