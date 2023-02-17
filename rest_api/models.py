from django.db import models

class Students (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name