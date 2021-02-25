from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.library.services.parser import get_all_books
from apps.library.services.getters import get_books_from_library
from requests.exceptions import Timeout


@api_view(['GET'])
def all_books(request):
    key_words = request.GET.get('q')
    if not key_words:
        return Response({'error': 'search field is empty'}, 400)
    html = get_books_from_library(key_words)

    try:
        result = get_all_books(html)
    except Timeout:
        return Response({'error': 'timeout'}, 504)

    return Response(result, 200)
