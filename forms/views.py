import json
from rest_framework import viewsets
from django.http import HttpResponse
from forms.serializers import (
    ApplicationFormConfigurationSerializer
)
from forms.models import (
    ApplicationFormConfiguration,
)
from forms.templates import APPLICATION_FORM_TEMPLATE_CONFIG

from forms.const import FORM_QUESTION_TYPES


class ApplicationFormViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationFormConfigurationSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     form_uuid = request.GET['form_uuid']
    #     queryset = ApplicationFormConfiguration.objects.get(uuid=form_uuid)
    #     return Response(self.serializer_class(queryset).data)


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
