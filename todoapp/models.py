from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)