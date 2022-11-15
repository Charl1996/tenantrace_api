import json
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import HttpResponse
from forms.serializers import (
    ApplicationFormConfigurationSerializer
)
from forms.models import (
    ApplicationFormConfiguration,
)
from forms.templates import APPLICATION_FORM_TEMPLATE_CONFIG
from forms.const import FORM_QUESTION_TYPES
from forms.schemas import CreateFormConfigSchema
from pydantic.error_wrappers import ValidationError


class ApplicationFormViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationFormConfigurationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        try:
            CreateFormConfigSchema(**data)
        except ValidationError:
            return HttpResponse(status=400, content="Invalid data")

        app_form_config = ApplicationFormConfiguration(
            config=data['config'],
            owner_email=data['email'],
        )
        app_form_config.save()

        return HttpResponse(
            content=json.dumps({'uuid': str(app_form_config.uuid)}),
            content_type="application/json",
        )

    def retrieve(self, request, *args, **kwargs):
        form_uuid = kwargs['uuid']
        queryset = ApplicationFormConfiguration.objects.get(uuid=form_uuid)
        return Response(self.serializer_class(queryset).data)


def form_templates(*args, **kwargs):
    return HttpResponse(
        content=json.dumps({'template': APPLICATION_FORM_TEMPLATE_CONFIG}),
        content_type='application/json',
    )


def form_question_types(*args, **kwargs):
    return HttpResponse(
        content=json.dumps({'types': FORM_QUESTION_TYPES}),
        content_type='application/json',
    )
