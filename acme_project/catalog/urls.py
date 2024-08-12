from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.product_list, name="products"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<slug:category>/", views.product_category),
]
