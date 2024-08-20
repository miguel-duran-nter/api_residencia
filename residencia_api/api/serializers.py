from rest_framework import serializers
from .models import User, Resident, Room, Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'date']

class ResidentSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)  # Incluye las actividades en el serializador de Resident

    class Meta:
        model = Resident
        fields = ['id', 'first_name', 'last_name', 'room', 'medical_info', 'activities']  # Incluye el campo activities

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'address']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'is_occupied']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'date']

class ResidentActivityUpdateSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all(),
        many=True
    )

    class Meta:
        model = Resident
        fields = ['activities']
