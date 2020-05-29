import api.models as models
import api.serializers as serializers
import api.services.utils as utils

from django.http import Http404


def get_all_groups_as_json():
    queryset = models.Group.objects.all()
    return serializers.GroupSerializers(queryset, many=True).data


def get_all_places_as_json():
    queryset = models.Place.objects.all()
    return serializers.PlaceSerializers(queryset, many=True).data


def get_all_professors_as_json():
    queryset = models.Professor.objects.all()
    return serializers.ProfessorSerializers(queryset, many=True).data


def get_hash(who):
    getter = {
            'groups': get_all_groups_as_json,
            'places': get_all_places_as_json,
            'professors': get_all_professors_as_json,
        }
    if who not in getter:
        raise Http404
    return utils.generate_hash(str(getter[who]()))


def get_current_week_evenness_as_json():
    current_week_evenness = utils.get_current_week_evenness()
    return {
        'isEven': str(current_week_evenness)
    }


def get_timetable_group_as_json(obj_id, week):
    queryset = models.TimetableGroup.objects.filter(group__id=obj_id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.TimetableSerializers(queryset, many=True).data


def get_timetable_place_as_json(obj_id, week):
    queryset = models.TimetablePlace.objects.filter(place__id=obj_id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.TimetableSerializers(queryset, many=True).data


def get_timetable_professor_as_json(obj_id, week):
    queryset = models.TimetableProfessor.objects.filter(professor__id=obj_id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.TimetableSerializers(queryset, many=True).data


def get_timetable(who, obj_id, week):
    getter = {
            'group': get_timetable_group_as_json,
            'place': get_timetable_place_as_json,
            'professor': get_timetable_professor_as_json,
        }
    if who in getter:
        return getter[who](obj_id, week)
    else:
        raise Http404
