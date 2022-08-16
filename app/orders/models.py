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
