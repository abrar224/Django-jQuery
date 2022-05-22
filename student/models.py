from django.db import models
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    batch = models.IntegerField()
    dept = models.CharField(max_length=20)