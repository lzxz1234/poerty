from django.db import models


class Ci(models.Model):
    value = models.AutoField(primary_key=True)
    rhythmic = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()