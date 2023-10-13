from django.db import models

# Create your models here.
class Book(models.Model):
    at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    doe = models.DateField()
    num_copies=models.IntegerField()

    def __str__(self):
        return self.title

 