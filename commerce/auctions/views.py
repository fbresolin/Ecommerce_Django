from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.values_list("pk", "title"),
    })


def my_listings(request):
    if request.user is not None:
        return render(request, "auctions/my_listings.html", {
            "listings": Listing.objects.filter(user=request.user).values_list("pk", "title"),
        })
    else:
        return HttpResponseRedirect(reverse("login"))




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, pk):
    return(render(request, "auctions/listing.html", {
        "listing_data": Listing.objects.get(pk=pk)
    }))
    ## pass listing_data = listing to HTML


def new_listing(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            listing = Listing(
                user=request.user,
                title=request.POST["title"],
                description=request.POST["description"],
                url=request.POST["image"],
                value=request.POST["value"],
            )
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=(listing.pk,)))
        else:
            return(render(request, "auctions/new_listing.html"))
    return HttpResponseRedirect(reverse("login"))
