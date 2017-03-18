from django.db import models


class Shi(models.Model):
    value = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()