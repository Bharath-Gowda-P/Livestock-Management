from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class stock(models.Model):
    
    id = models.CharField(max_length=5, primary_key=True)
    aclass = models.CharField(max_length=15)
    sex = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    insurance = models.DateField()
    vacstatus = models.CharField(max_length=10)
    vdate = models.CharField(max_length=10)
    ddate = models.DateField()

    def __str__(self):
        return self.aid