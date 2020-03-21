from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=40)
    done = models.BooleanField(default=False)
