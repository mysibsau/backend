import statistic.models as models


def collect_static(function):
    def warp(*args, **kwargs):
        url = args[1].get_full_path()

        stat = models.Statistics.objects.filter(url=url).first()
        if stat:
            stat.count += 1
            stat.save()
        else:
            models.Statistics(url=url, count=1).save()

        return function(*args, **kwargs)
    return warp
