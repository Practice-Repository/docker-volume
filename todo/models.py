from django.db import models

# Create your models here.
class ToDoData(models.Model):
    title = models.CharField(max_length=100)
