from django.db import models
from django.utils.text import slugify




# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.product.title
    


class ProductVariant(models.Model):
    variant_title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_product')
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.variant_title
    


class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variantprice_product')
    created_at = models.DateField(auto_now_add=True)