from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Item


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

    return JsonResponse(response_dict, safe=False, json_dumps_params={'indent': 4, 'ensure_ascii': False})
