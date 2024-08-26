from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    UserViewSet,
    ResidentViewSet,
    RoomViewSet,
    ActivityViewSet,
    ResidentActivityUpdateView,
    login_view,
    logout_view,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My Residence API",
        default_version="v1",
        description="API for management of residences",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="miguel.duran@nter.es"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"residents", ResidentViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"activities", ActivityViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/residents/<int:pk>/activities/",
        ResidentActivityUpdateView.as_view(),
        name="resident-activity-update",
    ),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    )
]
