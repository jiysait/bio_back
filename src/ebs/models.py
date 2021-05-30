from djongo import models


class Sequence(models.Model):
    seqfile_path = models.FileField(null=True, blank=True, upload_to='ebs/seq/')

    def __str__(self):
        return str(self.seqfile_path)


class Analysis(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    sequences = models.ManyToManyField(Sequence, related_name="usedin")

    def __str__(self):
        return str(self.name)
