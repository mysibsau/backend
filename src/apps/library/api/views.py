from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.library.services import getters


@api_view(['GET'])
def all_books(request):
    key_words = request.GET.get('q')
    if not key_words:
        return Response({'error': 'search field is empty'}, 400)
    key_words = key_words.strip().lower()

    return Response({
        'physical': getters.get_books(key_words, True),
        'digital': getters.get_books(key_words, False),
    }, 200)
