from django.db import models

class Account(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_name


# Create your models here.
