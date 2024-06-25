from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# class Choice(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     customisation = models.CharField(max_length=255)
#     allergens = models.BooleanField(default=False)
#     size = models.CharField(max_length=255)
#     collection_date = models.DateField()
#     collection_time = models.DateTimeField()

    def __str__(self):
        return self.title
