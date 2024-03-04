from django.db import models

# Create your models here.

class Form (models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
