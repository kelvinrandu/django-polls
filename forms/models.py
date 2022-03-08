from django.db import models

# Create your models here.
class Form(models.Model):
    name= models.CharField(max_length=150, blank=False)
 
    email = models.EmailField(('email'), blank=True, unique=True,
                                        help_text='254 characters or fewer. Must be a valid email address.')
    address=models.CharField(max_length=150, blank=False)
    computer_literate=models.BooleanField(('active'), default=True)
    income=models.CharField(max_length=150, blank=False)
    years_of_experience=models.PositiveSmallIntegerField(blank=True, null=True)