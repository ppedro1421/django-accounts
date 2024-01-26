import re
from rest_framework import serializers
from .models import *


class RegisterUserSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name', allow_null=True)
    profile = serializers.CharField(source='profile.name', allow_null=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'email', 'company', 'profile', 'password1', 'password2']

    def validate(self, attrs):
        password1 = attrs.get('password1', '')
        password2 = attrs.get('password2', '')

        if password1 != password2:
            raise serializers.ValidationError("password do not match")

        return attrs

    def create(self, validated_data):
        user = AuthUser()

        user.username = validated_data.get("username")
        user.email = validated_data.get("email")

        user.set_password(validated_data.get("password"))

        company = AuthCompany.objects.filter(id=validated_data.get("company")).first()
        profile = AuthUserProfile.objects.filter(id=validated_data.get("profile")).first()

        user.company = company
        user.profile = profile

        user.save()

        return validated_data
