from django.urls import path

from .views import get_item

urlpatterns = [
    path('items/<int:item_id>/', get_item, name='show_item'),
]
