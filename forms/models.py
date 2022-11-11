from django.db import models


class ApplicationFormConfiguration(models.Model):
    config = models.JSONField()
    owner_email = models.EmailField()


class ApplicationFormResponse(models.Model):
    application_form_configuration = models.ForeignKey(ApplicationFormConfiguration, on_delete=models.CASCADE, )
    value = models.JSONField()
