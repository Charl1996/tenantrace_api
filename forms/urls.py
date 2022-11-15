from django.urls import path
from forms.views import (
    form_question_types,
    form_templates,
    ApplicationFormViewSet,
)

form_config = ApplicationFormViewSet.as_view({'post': 'create'})
form_config_detail = ApplicationFormViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', form_config, name="form-config"),
    path('<uuid:uuid>', form_config_detail, name="form-config-detail"),
    path('templates', form_templates),
    path('question-types', form_question_types),
]
