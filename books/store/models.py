from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    author_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title}"