import binascii
import os

from django.db import models


class OrderBaseModel(models.Model):
    CREATED = 1
    IN_PROCESS = 2
    ARRIVED = 3
    FAILED = 4
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (IN_PROCESS, 'In process'),
        (ARRIVED, 'Arrived'),
        (FAILED, 'Failed'),
    )

    number = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountBaseModel(models.Model):
    token = models.CharField(max_length=40, primary_key=True)
    path = models.URLField(max_length=1024)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()
