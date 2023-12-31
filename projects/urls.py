from rest_framework import routers
from django.urls import path, include


from .views import ProfileViewSet, ProjectViewSet
from .views import CertificateViewSet, CertifyingInstitutionViewSet

router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("profiles/<int: id>", ProfileViewSet)
router.register("projects", ProjectViewSet)
router.register("projects/<int: id>", ProjectViewSet)
router.register("certifying-institutions", CertifyingInstitutionViewSet)
router.register("certificates", CertificateViewSet)


urlpatterns = [path("", include(router.urls))]
