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


def NotificationsSerializer(notification, context):
    request = context.get('request')
    result = []
    PRIORITIES = {
        5: 'normal',
        10: 'high'
    }
    for topic in notification.topics.all():
        priority = notification.priority
        priority = priority if topic.name[-3:] == 'ios' else PRIORITIES[priority]
        result.append({
            'notification': {
                'title': notification.title,
                'body': notification.text,
                'badge': 100
            },
            'to': f'/topics/{topic}',
            'priority': priority
        })
        if notification.image:
            result[-1]['image'] = request.build_absolute_uri(notification.image.url)
    return result
