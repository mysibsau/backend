import api.models as models
import api.serializers as serializers
import api.services.utils as utils

from django.http import Http404


def get_all_groups_as_json():
    queryset = models.Group.objects.all()
    return serializers.GroupSerializers(queryset, many=True).data


def get_hash():
    return utils.generate_hash(str(get_all_groups_as_json()))


def get_current_week_evenness_as_json():
    current_week_evenness = utils.get_current_week_evenness()
    return {
        'isEven': str(current_week_evenness)
    }


def get_timetable_group_as_json(obj_id, week):
    queryset = models.TimetableGroup.objects.filter(group__id=obj_id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.TimetableSerializers(queryset, many=True).data


def get_timetable(obj_id, week):
    return get_timetable_group_as_json(obj_id, week)
