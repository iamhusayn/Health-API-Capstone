from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
  # first_name = serializers.CharField(max_length=100)
  # last_name = serializers.CharField(max_length=100)
  # email = serializers.EmailField()

  class Meta:
    model = User
    fields = ['__all__']
  
  # def validate(self, data):
  #       if data['password'] != data['password2']:
  #           raise serializers.ValidationError({'password': 'Passwords must match'})
        
  #       validate_password(data['password'])
  #       return data
  
  # def create(self, validated_data):
  #   try:
  #     user = User.objects.get(
  #       first_name = validated_data['first_name'],
  #       last_name = validated_data['last_name'],
  #       email=validated_data['email']
  #     )
  #     raise serializers.ValidationError('User already exists')
  #     user.set_password(validated_data['password'])
  #     user.save()
  #     return user
  #   except Exception as e:
  #     raise serializers.ValidationError({'error': str(e)})
    
    # return User.objects.create(**validated_data)
  
  # def update(self, instance, validated_data):
  #   instance.first_name = validated_data.get('first_name', validated_data.first_name)
  #   instance.last_name = validated_data.get('last_name', validated_data.last_name)
  #   instance.email = validated_data.get('email', validated_data.email)

  #   return instance.save()

  # def __str__(self):
  #   return self.title