from django.db import models

# Create your models here.

class DayTemp(models.Model):
    date = models.DateField(unique=True)
    temp = models.FloatField()

    def __str__(self) -> str:
        return str(self.date) + ' ' + str(self.temp)