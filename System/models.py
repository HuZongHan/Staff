from django.db import models


# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField(default=True)

    class Meta:
        db_table = 'staff'


class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    tickek = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'users'
