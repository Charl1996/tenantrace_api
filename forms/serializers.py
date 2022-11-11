from rest_framework import serializers
from forms.models import (
    FormQuestionType,
    ApplicationFormConfiguration,
)


class FormQuestionTypeSerializer(serializers.Serializer):

    class Meta:
        model = FormQuestionType
        fields = ('type', 'display')


class ApplicationFormConfigurationSerializer(serializers.Serializer):

    class Meta:
        model = ApplicationFormConfiguration
        fields = ('config',)
