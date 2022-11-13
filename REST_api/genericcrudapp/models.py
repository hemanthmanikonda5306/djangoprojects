from django.db import models

# Create your models here.
class Gen(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    role = models.CharField(max_length=20)
    company = models.CharField(max_length=10)
    salary = models.FloatField()

    def __str__(self):
        return self.name