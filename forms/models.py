from ctypes import addressof
from unicodedata import name
from django.db import models

# Create your models here.
class Form(models.Model):
    name= models.TextField()
    email=models.TextField()
    address=models.TextField()
    computer_literate=models.TextField()
    income=models.TextField()