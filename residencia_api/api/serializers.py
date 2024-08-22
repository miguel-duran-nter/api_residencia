from rest_framework import serializers
from .models import User, Resident, Room, Activity
from django.contrib.auth import authenticate


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "name", "description", "date"]
        ref_name = "ActivitySerializer"


class ResidentSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(
        many=True, read_only=True
    )  # Incluye las actividades en el serializador de Resident

    class Meta:
        model = Resident
        fields = [
            "id",
            "first_name",
            "last_name",
            "room",
            "medical_info",
            "activities",
        ]
        ref_name = "Resident"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "address"]
        ref_name = "User"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "number", "is_occupied"]
        ref_name = "Room"


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "name", "description", "date"]
        ref_name = "ACtivity"


class ResidentActivityUpdateSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all(), many=True
    )

    class Meta:
        model = Resident
        fields = ["activities"]
        ref_name = "Resident_activity"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                raise serializers.ValidationError("Incorrect credentials")
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data["user"] = user
        return data
