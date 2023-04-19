from django.db import models

# Create your models here.


CATEGORY_CHOICES = (
    ("F", "FASHION"),
    ("E", "ELECTRONICS"),
    ("B", "BAGS"),
    ("C", "CLOTHES")
)

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="product_images", default="product.jpg")


    def __str__(self):
        return self.name