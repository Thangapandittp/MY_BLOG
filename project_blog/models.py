from django.db import models
from django.conf import settings

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    #image = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    image = models.ImageField(upload_to ='images/') 
