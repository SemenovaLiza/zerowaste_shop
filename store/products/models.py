from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """for admin."""
    title = models.CharField(
        'Category name',
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
        'Category',
        on_delete=models.PROTECT,
        related_name='category'
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Product(models.Model):
    """for users."""
    price = models.DecimalField(
        'Product price',
        max_digits=7,
        decimal_places=2
    )
    description = models.TextField(
        'Type of product',
        help_text='Type the product description'
    )
    type = models.ForeignKey(
        Type,
        blank=False,
        on_delete=models.PROTECT,
        related_name='type',
        verbose_name='Type of product',
        help_text='What type of product does your product belong to?'
    )
    seller = models.ForeignKey(
        User,
        'Seller',
        on_delete=models.CASCADE,
        related_name='seller',
        verbose_name='seller'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
