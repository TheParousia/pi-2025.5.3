from django.db import models


# Create your models here.
class FeedBack(models.Model):
    comentario = models.CharField(max_length=1000)