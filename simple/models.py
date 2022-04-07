from django.db import models
from datetime import date
# Create your models here.

class Email(models.Model):
    sender=models.CharField(max_length=50)
    receiver=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.CharField(null=True,max_length=1000)
    date=models.DateField()
        
    def __str__(self):
        return self.subject
    