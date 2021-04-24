from django.db import models

class BloodDonation(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    contact = models.CharField(max_length=10, null=True, blank=True)
    radio = models.CharField(max_length=200, null=True, blank=True)
    bloodGrp = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    disease = models.BooleanField(default=False)

    def __str__(self):
        return self.name

