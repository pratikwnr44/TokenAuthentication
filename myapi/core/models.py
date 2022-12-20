from django.db import models

# Create your models here.
class Snippet(models.Model):
    code = models.TextField()
    langauge = models.CharField(max_length=60)
    