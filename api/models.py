from django.db import models
from django.db.models import Q

#anotate  generar atributos
# Create your models here.
class ProductManager(models.Manager):
    def with_stock(self, min_stock=0, min_price=0):
        stock_filter=Q(stock__gt=min_stock)
        price_filter=Q(stock__gt=min_price)
        
        return self.filter(stock_filter & price_filter)
        

class Product(models.Model):
    name=models.CharField(
        null=False, blank=True, unique=True, max_length=255
    ) #varchar
    description= models.TextField(blank=True, null=True) #Text
    price= models.IntegerField(
        null=True,
        blank=True,
        default=0
    )
    stock= models.IntegerField(
        null=True,
        blank=True,
        default=0
    )

    created_at= models.DateTimeField(
        auto_now_add=True
    )

    category= models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='products'
    )

    objects=ProductManager()

    def __str__(self):
        return self.name
    

