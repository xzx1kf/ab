from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Court(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    def __str__(self):
        return self.name + " - " + self.club.name

class Slot(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateTimeField()
    booked = models.BooleanField(default=False)
    def __str__(self):
        return self.court.name + " @" + self.date.strftime('%d/%m/%Y %H:%M')
