from django.db import models

# Create your models here.
class todolist(models.Model):
    item_title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    item_price = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.item_title