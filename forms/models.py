from ctypes import addressof
from unicodedata import name
from django.db import models

# Create your models here.
class Form(models.Model):
    name= models.CharField(max_length=150, blank=False)
 
    email = models.EmailField(('email'), blank=True, unique=True,
                                        help_text='254 characters or fewer. Must be a valid email address.')
    address=models.TextField()
    computer_literate=models.BooleanField(('active'), default=True)
    income=models.TextField()
    years_of_experience = models.PositiveSmallIntegerField(blank=True, null=True)