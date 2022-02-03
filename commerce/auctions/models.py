from ast import Pass
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    url = models.URLField(max_length=200)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.user}: {self.listing} and value {self.value}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.user}: {self.comment}"


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.listing}"
