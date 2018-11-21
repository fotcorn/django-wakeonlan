from django.db import models
from django.core.validators import RegexValidator

mac_address_validator = RegexValidator(regex='^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')

class Target(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100, validators=[mac_address_validator])

    def __str__(self):
        return self.name
