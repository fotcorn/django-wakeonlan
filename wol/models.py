from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
