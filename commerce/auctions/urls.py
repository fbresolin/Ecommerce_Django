from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:pk>", views.listing, name="listing"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("edit_listing/<int:pk>", views.edit_listing, name="edit_listing"),
    path("delete_listing", views.delete_listing, name="delete_listing"),
    path("listings/<str:user>", views.listings, name="listings"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("bid", views.bid, name="bid"),
    path("comment", views.comment, name="comment"),    
]
