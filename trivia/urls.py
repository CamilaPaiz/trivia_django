from django.urls import path, include
from .views import QuestionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
