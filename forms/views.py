from rest_framework import viewsets
from forms.serializers import (
    FormQuestionTypeSerializer,
    ApplicationFormConfigurationSerializer
)
from forms.models import (
    FormQuestionType,
    ApplicationFormConfiguration,
)


class ApplicationFormTemplateViewSet(viewsets.ModelViewSet):
    queryset = ApplicationFormConfiguration.objects.filter(is_template=True)
    serializer_class = ApplicationFormConfigurationSerializer


class FormQuestionTypeViewSet(viewsets.ModelViewSet):
    queryset = FormQuestionType.objects.all()
    serializer_class = FormQuestionTypeSerializer


def create_new_form():
    return []
