from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Test(models.Model):
    
    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    owner = models.ManyToManyField(User, related_name ="test")
    
    def __str__(self):
        return self.name

class Functions(models.Model):
    
    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    owner = models.ManyToManyField(Test, related_name ="Functions")

    def __str__(self):
        return self.name