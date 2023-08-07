from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime


class User_info(models.Model): #every models has a manager default called object and is used accessing a query set from the database
    name = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    extra = models.CharField(max_length=500)
    date = models.DateField(default=datetime.utcnow())

