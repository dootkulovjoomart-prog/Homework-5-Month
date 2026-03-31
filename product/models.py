from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null = True)

    def __str__(self):
        return f'{self.title}'

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null = True)

    def __str__(self):
        return f'{self.product}'
