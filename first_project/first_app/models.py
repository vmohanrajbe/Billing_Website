from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return str(self.top_name)

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.PROTECT)
    date = models.DateField()

    def _str__(self):
        return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    Last_name = models.CharField(max_length=264,unique=True)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Email
