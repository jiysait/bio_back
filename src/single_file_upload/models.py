# from django.db import models
from djongo import models

# Create your models here.


class SingleFileUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to="")

    def __str__(self):
        return self.title
