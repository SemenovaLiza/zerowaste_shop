from django.db import models


class Product(models.Model):
    product = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(
        'description',
        help_text='Describe the product.'
    )
    # seller =
    # reviews =

class Categories(models.Model):
    slug = models.SlugField(unique=True)


class Sort(models.Model):
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='sorts',
        verbose_name='sort of product',
        help_text='Сhoose the sort of the product.'
    )
    products = models.ForeignKey(
        Product,
        null=True,
        related_name='sort',
        verbose_name='product'
    )
