from .. import models


def UserTicketsSerializer(purchases):
    result = []
    for purchase in purchases:
        result.append({
            'id': purchase.id,
            'buyer': purchase.buyer,
            'product': purchase.product,
            'count': purchase.count,
            'datetime': purchase.datetime,
            'code': purchase.code,
            'status': purchase.status
        })
    return result