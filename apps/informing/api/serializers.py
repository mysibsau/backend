from .. import models


def EventsSerializers(events, liked):
    result = []
    for event in events:
        result.append({
            'id': event.id,
            'name': event.name,
            'logo': {
                'url': event.logo.url,
                'width': event.logo.width,
                'height': event.logo.height
            },
            'text': event.text,
            'views': event.views,
            'likes': event.likes,
            'is_liked': event.id in liked
        })
    return result


def ImagesSerializer(images):
    result = []
    for image in images:
        result.append({
            'url': image.image.url,
            'width': image.image.width,
            'height': image.image.height
        })
    return result


def NewsSerializer(news_queryset, liked):
    result = []
    for news in news_queryset:
        images = models.Image.objects.filter(news__id=news.id)
        result.append({
            'id': news.id,
            'text': news.text,
            'views': news.views,
            'likes': news.likes,
            'is_liked': news.id in liked,
            'images': ImagesSerializer(images)
        })
    return result
