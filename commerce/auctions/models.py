from ast import Pass
from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timezone


class User(AbstractUser):
    pass


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    url = models.URLField(max_length=200)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(default=datetime.now(timezone.utc))

    def __str__(self):
        return self.title

    def time_elapsed_since_created(self):
        deltatime = datetime.now(timezone.utc) - self.created
        if (deltatime.seconds/3600) < 23:
            return f"{round(deltatime.seconds/3600)} hours"
        else:
            return f"{deltatime.days} days"

    def get_highest_bid(self):
        return Bid.objects.filter(listing=self).values_list("value", flat=True).last()

    def get_bid_count(self):
        return Bid.objects.filter(listing=self).count()

    def get_bid_username(self):
        highest_bid = Bid.objects.filter(listing=self).last()
        if highest_bid is not None:
            return highest_bid.user.username
        else:
            return None


    def get_bid_email(self):
        highest_bid = Bid.objects.filter(listing=self).last()
        if highest_bid is not None:
            return highest_bid.user.email
        else:
            return None


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(default=datetime.now(timezone.utc))

    def __str__(self):
        return f"{self.user}: {self.listing} and value {self.value}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    created = models.DateTimeField(default=datetime.now(timezone.utc))

    def __str__(self):
        return f"{self.user}: {self.comment}"

    def get_last_comments(self):
        return Comment.filter(listing=self).sort('created')

    def time_elapsed_since_created(self):
        deltatime = datetime.now(timezone.utc) - self.created
        if (deltatime.seconds/3600) < 23:
            return f"{round(deltatime.seconds/3600)} hours"
        else:
            return f"{deltatime.days} days"


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    wish = models.BooleanField()

    def __str__(self):
        return f"{self.user}: {self.listing} {self.wish}"
