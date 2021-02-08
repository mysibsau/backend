from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def auth(request):
    return Response({
        "token": "12345tyrdsw4r",
        "FIO": "Василий П. Н.",
        "averga": 4.7,
        "group": "БПЫ228-03",
        "zachotka": "18731042",
    })
