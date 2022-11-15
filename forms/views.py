import json
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from forms.serializers import (
    ApplicationFormConfigurationSerializer
)
from forms.models import (
    ApplicationFormConfiguration,
    ApplicationFormResponse,
)
from forms.templates import APPLICATION_FORM_TEMPLATE_CONFIG
from forms.const import FORM_QUESTION_TYPES
from forms.schemas import CreateFormConfigSchema
from pydantic.error_wrappers import ValidationError
from tenantrace_api.mailer import send_application_response_email


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

    def add_response(self, request, *args, **kwargs):
        response_data = request.data.get('response')
        config_uuid = str(kwargs['uuid'])
        config = ApplicationFormConfiguration.objects.get(uuid=config_uuid)

        if not config:
            return HttpResponse(
                status=404,
                content=json.dumps({"error": "Configuration not found"})
            )

        response_object = ApplicationFormResponse(
            application_form_configuration=config,
            value=response_data
        )
        response_object.save()

        try:
            send_application_response_email(config.owner_email, response_object)
        except Exception as e:
            return HttpResponse(status=400, content=json.dumps({"error": e}))

        return HttpResponse(status=200, content=json.dumps({"success": True}))


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
