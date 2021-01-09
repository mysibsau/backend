from .. import models


def EventsSerializers(events):
    result = []
    for event in events:
        result.append({
            'name': event.name,
            'logo': {
                'url': event.logo.url,
                'width': event.logo.width,
                'height': event.logo.height
            },
            'text': event.text,
            'views': event.views,
            'likes': event.count_likes()
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


def NewsSerializer(news_queryset):
    result = []
    for news in news_queryset:
        images = models.Image.objects.filter(news__id=news.id)
        result.append({
            'text': news.text,
            'views': news.views,
            'likes': news.count_likes(),
            'images': ImagesSerializer(images)
        })
    return result
