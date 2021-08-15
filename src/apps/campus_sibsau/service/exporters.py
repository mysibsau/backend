import csv
from urllib.parse import quote

from django.db.models import QuerySet
from django.db.models import DateTimeField
from django.http import HttpResponse
from django.utils import timezone

from apps.campus_sibsau.models import JoiningEnsemble


def export_as_csv(queryset: QuerySet[JoiningEnsemble]) -> HttpResponse:
    meta = queryset.model._meta

    response = HttpResponse(content_type='text/csv; charset=windows-1251')
    response['Content-Disposition'] = f'attachment; filename={quote(meta.verbose_name_plural)} {timezone.localtime().date()}.csv'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(field.verbose_name for field in meta.fields)

    for obj in queryset:
        fields = []
        for field in meta.fields:
            data = obj.__getattribute__(field.name)
            if type(field) == DateTimeField:
                print(data, type(data))
                data = data.strftime('%Y-%m-%d %H:%M:%S')
            fields.append(data)
        writer.writerow(fields)

    return response
