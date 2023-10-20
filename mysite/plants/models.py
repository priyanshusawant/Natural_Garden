from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, 
        default="https://i.pinimg.com/736x/fa/d3/4a/fad34a707359c5c1bfe1a4461010b7a1.jpg"
    )

    def __str__(self):
        return self.item_name