from django.db import models

class Employees (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name