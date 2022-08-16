from django.db import models


class AccountBaseModel(models.Model):
    token = models.CharField(max_length=40, primary_key=True)
    path = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
