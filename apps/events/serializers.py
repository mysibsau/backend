from apps.events.models import models


def LinkSerializers(links):
    result = []
    for link in links:
        result.append({
            'name': link.name,
            'link': link.link
        })
    return result


def EventSeializers(events):
    result = []
    for event in events:
        links = models.Link.objects.filter(event__id=event.id)
        result.append({
            'name': event.name,
            'logo': event.logo.url,
            'text': event.text,
            'author': event.author,
            'links': LinkSerializers(links)
        })
    return result
