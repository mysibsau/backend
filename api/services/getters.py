import api.models as models
import api.serializers as serializers


def get_all_groups_as_json():
    queryset = models.Group.objects.all()
    return serializers.GroupSerializers(queryset, many=True).data


def get_all_places_as_json():
    queryset = models.Place.objects.all()
    return serializers.PlaceSerializers(queryset, many=True).data


def get_all_professors_as_json():
    queryset = models.Professor.objects.all()
    return serializers.ProfessorSerializers(queryset, many=True).data


def get_timetable_group_as_json(id, week):
    queryset = models.TimetableGroup.objects.filter(group__id=id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.GroupTimetableSerializers(queryset, many=True).data


def get_timetable_place_as_json(id, week):
    queryset = models.TimetablePlace.objects.filter(place__id=id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.PlaceTimetableSerializers(queryset, many=True).data


def get_timetable_professor_as_json(id, week):
    queryset = models.TimetableProfessor.objects.filter(professor__id=id).distinct()
    queryset = queryset.filter(even_week=((week+1) % 2))
    return serializers.ProfessorTimetableSerializers(queryset, many=True).data