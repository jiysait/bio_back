# from django.db import models
from djongo import models


# Create your models here.
class MyFile(models.Model):
    # name = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to='sfu/')

    def __str__(self):
        return str(self.file)
