from django.db import models

# Create your models here.
class contactform(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    query = models.TextField()
