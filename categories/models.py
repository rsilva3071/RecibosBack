from django.db import models
from django.db.models import Count,When, Case, Value

class CategoryManager(models.Manager):
    def with_is_active(self):
        self.annotate(
            total_product=Count('products') 
        ).annotate(
            is_active=Case(
                When(total_products__gt=0, then=Value(True)),
                default=False
            )
        )


# Create your models here.
class Category(models.Model):
    name= models.CharField(
        max_length=50
    )

    objects=CategoryManager()


    def __str__(self):
        return self.name