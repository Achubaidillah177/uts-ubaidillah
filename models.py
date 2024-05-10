from django.db import models

# Create your models here.
class Bengkel (models.Model):
    title = models.CharField(max_length=100)
    numer_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.ImageField()

    def __str__(self):
        return self.title
    


    
#   /Bengkel/list