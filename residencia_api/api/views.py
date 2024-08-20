from rest_framework import viewsets
from .models import User, Resident, Room, Activity
from .serializers import UserSerializer, ResidentSerializer, RoomSerializer, ActivitySerializer, ResidentActivityUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all().order_by('first_name')
    serializer_class = ResidentSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ResidentActivityUpdateView(generics.UpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentActivityUpdateSerializer

    def update(self, request, *args, **kwargs):
        resident = self.get_object()
        serializer = self.get_serializer(resident, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # Retrieve the updated resident to include the activities in the response
        updated_resident = self.get_object()
        updated_serializer = self.get_serializer(updated_resident)
        return Response(updated_serializer.data)