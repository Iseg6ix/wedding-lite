from django.db import models

class Bride(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    bridesmaid = models.CharField(max_length=100)

class Groom(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    bestman = models.CharField(max_length=100)