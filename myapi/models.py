from django.db import models

# Create your models here.
class Cake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    desc = models.CharField(max_length=255)
    upload = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.name