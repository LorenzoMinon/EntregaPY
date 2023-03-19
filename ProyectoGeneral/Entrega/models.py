from django.db import models

# Create your models here.

# Modelos 


class Libro(models.Model):

    title = models.CharField(max_length=40)
    publicationdate = models.DateField()
    author= models.CharField(max_length=40)


class Autor(models.Model):

    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    number = models.IntegerField()
    
class Editor(models.Model):
    
    name = models.CharField(max_length=40)
    adress = models.CharField(max_length=40)
    website = models.CharField(max_length=240)


