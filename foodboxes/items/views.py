from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item


@api_view(['GET'])
def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    response_dict = {
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'image': item.image.url,
        'weight': item.weight,
        'price': item.price,

    }

    return Response(response_dict)
