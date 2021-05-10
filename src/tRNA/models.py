from django.db import models

# Create your models here.
class tRNA(models.Model):
    gene = models.CharField(max_length=200)
    contig = models.CharField(max_length=200)
    start = models.IntegerField()
    end = models.IntegerField()
    length = models.IntegerField()
