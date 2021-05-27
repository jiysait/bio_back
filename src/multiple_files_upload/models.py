from djongo import models


class MyFile(models.Model):
    file = models.FileField(null=True, blank=True, upload_to='mfu/')

    def __str__(self):
        return str(self.file)
