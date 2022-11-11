from django.urls import path, include
from rest_framework import routers
from forms.views import (
    form_question_types,
    form_templates,
    ApplicationFormViewSet,
)

router = routers.DefaultRouter()
router.register(r'', ApplicationFormViewSet, basename="create_form_config")
# router.register(r'(?P<form_uuid>\d+)/$', ApplicationFormViewSet, basename="retrieve_form_by_id")

urlpatterns = [
    path('', include(router.urls)),
    path('templates', form_templates),
    path('question-types', form_question_types),
]
