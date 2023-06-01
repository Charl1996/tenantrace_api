from django.db import models
import uuid


class ApplicationFormConfiguration(models.Model):
     config = models.JSONField()
    owner_email = models.EmailField()
    uuid = models.UUIDField(default=uuid.uuid4)


class ApplicationFormResponse(models.Model):
    application_form_configuration = models.ForeignKey(ApplicationFormConfiguration, on_delete=models.CASCADE, )
    value = models.JSONField()
