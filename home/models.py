from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name