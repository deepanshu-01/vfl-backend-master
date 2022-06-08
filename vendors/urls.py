from django.urls import path
from .views import VendorView, VendorCreateView, VendorListView, VendorSpecificListView

urlpatterns=[
    path('vendor/<int:pk>/', VendorView.as_view()),
    path('vendor/create/', VendorCreateView.as_view()),
    path('vendor/', VendorListView.as_view()),
    path('vendor/specific/', VendorSpecificListView.as_view()),
]