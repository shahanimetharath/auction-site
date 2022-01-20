from django.urls import re_path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    re_path("", views.index, name="index"),
    re_path("login", views.login_view, name="login"),
    re_path("logout", views.logout_view, name="logout"),
    re_path("register", views.register, name="register"),
    re_path("create", views.createlisting, name="create"),
    re_path("category", views.category, name="category"),
    re_path("listing/<int:id>", views.listingpage, name="listingpage"),
    re_path("listing/<int:id>/addwatch",views.addwatch,name="addwatch"),
    re_path("listing/<int:id>/removewatch",views.removewatch,name="removewatch"),
    re_path("listing/<int:listingid>/bid",views.bid,name="bid"),
    re_path("listing/<int:listingid>/closebid",views.closebid,name="closebid"),
    re_path("watchlist", views.watchlist, name="watchlist"),
    re_path("listing/<int:listingid>/closed", views.closed, name="closed"),
    re_path("comment/<int:listingid>", views.comment, name="comment"),
    re_path("category", views.category, name="category"),
    re_path("category/<str:cats>", views.categorylistings, name="categorylistings"),   
    re_path("listing/closed", views.allclosed, name="allclosed"),
]
