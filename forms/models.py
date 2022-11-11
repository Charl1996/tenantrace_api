from django.db import models


class FormQuestionType(models.Model):
    type = models.CharField(max_length=200)
    display = models.CharField(max_length=200)

    # Need to prepopulate the model with the following values:
    # {type: "checkbox", display: "Checkbox"},
    # // {type: "date", display: "Date"},
    # {type: "dropdown", display: "Dropdown"},
    # {type: "file", display: "File upload"},
    # // {type: "radio", display: "Multiple choice"},
    # {type: "tel", display: "Contact number"},
    # {type: "text", display: "Short response"},
    # {type: "textarea", display: "Long response"},


class ApplicationFormConfiguration(models.Model):
    config = models.JSONField()
    is_template = models.BooleanField(default=False)
    owner_email = models.EmailField()


class ApplicationFormResponse(models.Model):
    application_form_configuration = models.ForeignKey(ApplicationFormConfiguration, on_delete=models.CASCADE, )
    value = models.JSONField()
