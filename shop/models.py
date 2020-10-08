from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=40)
    category = models.CharField(max_length=40, default="")
    subcategory = models.CharField(max_length=40, default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


