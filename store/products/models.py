from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """for admin."""
    title = models.CharField(
        verbose_name='Category name',
        max_length=200
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Type(models.Model):
    """for admin."""
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category',
        verbose_name='Category'
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Product(models.Model):
    """for users."""
    price = models.DecimalField(
        verbose_name='Product price',
        max_digits=7,
        decimal_places=2
    )
    description = models.TextField(
        verbose_name='Type of product',
        help_text='Type the product description'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name='type',
        blank=False,
        verbose_name='Type of product',
        help_text='What type of product does your product belong to?'
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='Seller'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
