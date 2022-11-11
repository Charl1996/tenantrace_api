from django.urls import path, include
from rest_framework import routers
from forms.views import (
    ApplicationFormTemplateViewSet,
    FormQuestionTypeViewSet,
)

router = routers.DefaultRouter()
router.register(r'template', ApplicationFormTemplateViewSet)
router.register(r'question-types', FormQuestionTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
