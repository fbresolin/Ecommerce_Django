from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from decimal import Decimal
from django.contrib import messages
from .models import User, Listing, Wish, Bid, Comment


def index(request):
    return render(request, "auctions/listings.html", {
        "listings_data": Listing.objects.all(),
        "listing_type": "index",
    })


def listings(request, user):
    return render(request, "auctions/listings.html", {
        "listings_data": Listing.objects.filter(user=User.objects.get(username=user)),
        "listing_type": "user",
    })


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
    listing_data = Listing.objects.get(pk=pk)
    comments = Comment.objects.filter(listing=listing_data)
    if request.user.is_authenticated:
        wishobj = Wish.objects.filter(
            user=request.user, listing=listing_data).first()
        if wishobj is None:
            wish = False
        else:
            wish = wishobj.wish
    else:
        wish = ""
    return(render(request, "auctions/listing.html", {
        "listing_data": listing_data,
        "wish": wish,
        "comments": comments,
    }))


def new_listing(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            listing = Listing(
                user=request.user,
                title=request.POST["title"],
                description=request.POST["description"],
                url=request.POST["image"],
                value=request.POST["value"]
            )
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=(listing.pk,)))
        else:
            return(render(request, "auctions/new_listing.html"))
    return HttpResponseRedirect(reverse("login"))


def edit_listing(request, pk):
    listing_data = Listing.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == listing_data.user:
        if request.method == "POST":
            listing_data.title = request.POST["title"]
            listing_data.description = request.POST["description"]
            listing_data.url = request.POST["image"]
            listing_data.value = request.POST["value"]
            listing_data.save()
            return HttpResponseRedirect(reverse("listing", args=(pk,)))
        else:
            return(render(request, "auctions/edit_listing.html", {
                "listing_data": listing_data,
            }))
    return HttpResponseRedirect(reverse("login"))


def delete_listing(request):
    listing_data = Listing.objects.get(pk=request.POST["pk"])
    if request.user.is_authenticated and request.user == listing_data.user:
        listing_data.delete()
    return HttpResponseRedirect(reverse("index"))


def wishlist(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            listing_data = Listing.objects.get(pk=request.POST["pk"])
            Wish.objects.filter(user=request.user,
                                listing=listing_data).delete()
            wish = 1 - int(request.POST["wish"])
            wishobj = Wish(
                user=request.user,
                listing=Listing.objects.get(pk=request.POST["pk"]),
                wish=bool(wish)
            )
            wishobj.save()
            return HttpResponseRedirect(reverse("listing", args=(request.POST["pk"],)))
        wishlist_pks = Wish.objects.filter(
            user=request.user, wish=True).values_list('listing', flat="True")
        wishlist = Listing.objects.filter(
            pk__in=wishlist_pks)
        return render(request, "auctions/listings.html", {
            "listings_data": wishlist,
            "listing_type": "wishlist",
        })
    return HttpResponseRedirect(reverse("login"))


def bid(request):
    listing_data = Listing.objects.get(pk=request.POST["pk"])
    actual_bid = listing_data.get_highest_bid()
    if request.user.is_authenticated and request.user != listing_data.user:
        if (actual_bid is None) or (Decimal(request.POST["bid"]) > actual_bid):
            bid = Bid(
                user=request.user,
                listing=listing_data,
                value=request.POST["bid"]
            )
            bid.save()
            messages.success(
                request, f"Your bid was accepted successfully")
        else:
            messages.warning(
                request, f"Proposed bid is smaller than the current bid, please give a bid higher than R${actual_bid}")
    return HttpResponseRedirect(reverse("listing", args=(request.POST["pk"],)))


def comment(request):
    listing_data = Listing.objects.get(pk=request.POST["pk"])
    if request.user.is_authenticated:
        comment = Comment(
            user=request.user,
            listing=listing_data,
            comment=request.POST["comment"]
        )
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=(request.POST["pk"],)))
    else:
        return HttpResponseRedirect(reverse("login"))
