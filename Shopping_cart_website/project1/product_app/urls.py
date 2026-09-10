from product_app import views
from django.urls import path

urlpatterns = [
    path("", views.product_show),
    path("showid/", views.showId)
]