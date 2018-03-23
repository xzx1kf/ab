from django.db import models

# Create your models here.
class Court(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

class Slot(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateTimeField()
    booked = models.BooleanField(default=False)
