from django.db import models

# Create your models here.

from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='file_uploads/')
    # default='default.txt',