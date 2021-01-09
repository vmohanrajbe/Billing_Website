from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    Last_name = models.CharField(max_length=264,unique=True)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Email
