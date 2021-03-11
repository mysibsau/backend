from typing import List
from apps.shop.models import Purchase


def UserTicketsSerializer(purchases: List[Purchase]) -> List[dict]:
    result = []
    for purchase in purchases:
        result.append({
            'id': purchase.id,
            'buyer': purchase.buyer,
            'product': purchase.product,
            'count': purchase.count,
            'datetime': purchase.datetime,
            'code': purchase.code,
            'status': purchase.status,
        })
    return result
