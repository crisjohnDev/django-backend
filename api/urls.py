from django.urls import path
from .views import items, delete_item

urlpatterns = [
    path('items/', items),
    path('delete/<int:id>/', delete_item),
]