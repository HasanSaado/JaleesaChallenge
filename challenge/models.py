from django.db import models

# Create your models here.

class Babysitter(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    birth = models.DateField()

    def __str__(self):
        return self.name