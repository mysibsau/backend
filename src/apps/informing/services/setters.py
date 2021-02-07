from apps.informing import models


def like_it(uuid, information):
    like = models.Like.objects.filter(
        uuid=uuid,
        information=information
    ).first()

    if like:
        like.delete()
        return {'good': 'лайк убран'}, 200

    models.Like.objects.create(
        uuid=uuid,
        information=information
    )
    return {'good': 'лайк поставлен'}, 200
