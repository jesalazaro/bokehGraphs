from django.db import models

class Hospitalizations(models.Model):
    HospiWeeks = models.IntegerField()
    HospiPati = models.IntegerField()

    def __str__(self):
        return "{}-{}.format(self.HospiWeeks self.HospiPati)"
# Create your models here.


# Create your models here.
