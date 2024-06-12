from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'affiliation', 'password', 'gender'
        )

    def create(self, validated_data):
        """
        user create bo'layotganda password-ni hashlab ketish
        """
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        user data update bo'layotganda password-ni hashlab ketish
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
