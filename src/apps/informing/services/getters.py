from apps.informing import models


def get_ids_liked_information_for_uuid(uuid):
    return [
        elem.information.id for elem in
        models.Like.objects.filter(uuid=uuid)
    ]
