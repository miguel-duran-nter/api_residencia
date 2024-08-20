from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ResidentViewSet, RoomViewSet, ActivityViewSet, ResidentActivityUpdateView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'residents', ResidentViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include('api.urls')),
    path('api/residents/<int:pk>/activities/', ResidentActivityUpdateView.as_view(), name='resident-activity-update'),
]