from django.urls import path
from . import views

urlpatterns = [
    path('create-fetch/', views.ProductsListCreateView.as_view(),
         name="product-list-create-view"),
    path('update-delete/<int:pk>/', views.ProductsUpdateDeleteView.as_view(),
         name="product-update-delete-view")
]
