from rest_framework import viewsets
from .models import User, Resident, Room, Activity
from .serializers import UserSerializer, ResidentSerializer, RoomSerializer, ActivitySerializer, ResidentActivityUpdateSerializer, LoginSerializer
from .mixins import LoggedInCookieMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
import json

class UserViewSet(LoggedInCookieMixin, viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ResidentViewSet(LoggedInCookieMixin, viewsets.ModelViewSet):
    queryset = Resident.objects.all().order_by('first_name')
    serializer_class = ResidentSerializer

class RoomViewSet(LoggedInCookieMixin, viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('number')
    serializer_class = RoomSerializer

class ActivityViewSet(LoggedInCookieMixin, viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('id')
    serializer_class = ActivitySerializer

class ResidentActivityUpdateView(LoggedInCookieMixin, generics.UpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentActivityUpdateSerializer

    def update(self, request, *args, **kwargs):
        resident = self.get_object()
        serializer = self.get_serializer(resident, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updated_resident = self.get_object()
        updated_serializer = self.get_serializer(updated_resident)
        return Response(updated_serializer.data)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            response = JsonResponse({"detail": f"Login successful {user.username}"})
            response.set_cookie('logged', 'true')
            return response
        else:
            return JsonResponse({"detail": "Invalid credentials"}, status=401)
    return JsonResponse({"detail": "Method not allowed"}, status=405)

@csrf_exempt
def logout_view(request):
    response = JsonResponse({"detail": "Logged out successfully"})
    response.delete_cookie('logged')
    return response