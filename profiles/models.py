from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=80,
                                 null=True, blank=True)
    lastname = models.CharField(max_length=80, null=True, blank=True)
    phone_number = models.CharField(max_length=20,
                                    null=True, blank=True)
    address1 = models.CharField(max_length=80,
                                null=True, blank=True)
    address2 = models.CharField(max_length=80,
                                null=True, blank=True)
    town_or_city = models.CharField(max_length=40,
                                    null=True, blank=True)
    county = models.CharField(max_length=80,
                              null=True, blank=True)
    postcode = models.CharField(max_length=20,
                                null=True, blank=True)
    email = models.CharField(max_length=254,
                             null=True, blank=True)

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
