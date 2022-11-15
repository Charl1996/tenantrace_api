from rest_framework import serializers
from forms.models import (
    ApplicationFormConfiguration,
)


class ApplicationFormConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationFormConfiguration
        fields = ('config', 'uuid')
