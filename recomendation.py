from apps.timetable.models import Timetable, Lesson
from apps.timetable.serializers import TimetableSerializers

GROUP = 'РС18-01'
TIMES = [
    '08:00-09:30', '09:40-11:10', '11:30-13:00', '13:30-15:00',
    '15:10-16:40', '16:50-18:20', '18:30-20:00', '20:10-21:40'
]

LIKES_TAGS = ['программирование', 'техника', 'физика', 'ракета', 'информация', 'разработка', 'эксперимент']
MAX_LESSONS = 2

timetable = Timetable.objects.filter(group__name=GROUP)
recomend_timetable = Timetable.objects.filter(lesson__tags__name__in=LIKES_TAGS, lesson_type=1)
result = list(timetable)

print(len(timetable))
count = 0

def get_best(lessons):
    lessons.sort(key=lambda x: len(x.lesson.tags.all()), reverse=True)
    return lessons[0]

for week in range(1, 3):
    for day in range(7):
        for time in TIMES:
            if timetable.filter(week=week, day=day, time=time) or count >= MAX_LESSONS:
                continue
            t = recomend_timetable.filter(week=week, day=day, time=time)
            if not t:
                continue
            t = get_best(list(t))
            print(week, day, time, t.lesson.name_ru)
            result.append(t)
            count += 1
        count = 0        

