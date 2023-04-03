from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    cid=models.IntegerField()
    Client=models.CharField(max_length=20)
    date=models.DateField()
    user=models.CharField(max_length=20)


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.id})
