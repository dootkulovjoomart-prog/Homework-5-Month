from django.db import models
from user.models import CustomUser
from common.models import BaseModel
# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=50)



    def __str__(self):
        return f'{self.name}'

class Product(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null = True , related_name='products')
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)

    def category_list(self):
        return  self.category.name if self.category else None
   
   
   
    def rating(self):
        reviews = self.reviews.all()
        count=self.reviews.all().count()
        if not reviews :
            return 0
        total = 0
        for i in reviews:
            total += i.stars
        return total /count

    def __str__(self):
        return f'{self.title}'
    
class Review(BaseModel):
    text = models.TextField()
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null = True , related_name='reviews')
    stars = models.IntegerField( choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')] )




    def __str__(self):
        return f'{self.product}'
