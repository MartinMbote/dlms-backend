
from rest_framework import serializers
from .models import CustomUser, StudentProfile, TutorProfile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

class StudentRegistrationSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = CustomUser.objects.create_user(**validated_data)
        StudentProfile.objects.create(user=user, **profile_data)
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['profile'] = StudentProfileSerializer(instance.student_profile).data
        return representation
    
class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorProfile
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

class TutorRegistrationSerializer(serializers.ModelSerializer):
    profile = TutorProfileSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = CustomUser.objects.create_user(**validated_data)
        TutorProfile.objects.create(user=user, **profile_data)
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['profile'] = TutorProfileSerializer(instance.tutor_profile).data
        return representation
