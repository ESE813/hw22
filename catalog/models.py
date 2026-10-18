from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    photo = models.ImageField(upload_to='photos/')
    category = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='products')




    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'





class Category(models.Model):
    name = models.CharField
    description = models.TextField
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f"{self.name} {self.description}"


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'




