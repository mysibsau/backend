from django.test import TestCase
import api.models as models
import api.serializers as serializers

class GroupSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Group.objects.create(
            name='БПИ18-01',
            mail='test@sibsau.ru'
        )

    def test_contains_expected_fields(self):
        fields = ['id', 'name', 'mail']
        group = models.Group.objects.all()[0]
        data = serializers.GroupSerializers(group).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_name_field_content(self):
        group = models.Group.objects.all()[0]
        data = serializers.GroupSerializers(group).data
        self.assertEquals(data['name'], 'БПИ18-01')

    def test_mail_field_content(self):
        group = models.Group.objects.all()[0]
        data = serializers.GroupSerializers(group).data
        self.assertEquals(data['mail'], 'test@sibsau.ru')


class ProfessorSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Professor.objects.create(
            name='Фамилия Имя Отчество',
            mail='fio@sibsau.ru',
            phone='+79631859823',
            department = 'ИИТК'
        )

    def test_contains_expected_fields(self):
        fields = ['id', 'name', 'mail', 'phone', 'department']
        professor = models.Professor.objects.all()[0]
        data = serializers.ProfessorSerializers(professor).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_mail_field_content(self):
        group = models.Professor.objects.all()[0]
        data = serializers.ProfessorSerializers(group).data
        self.assertEquals(data['mail'], 'fio@sibsau.ru')

    def test_phone_field_content(self):
        group = models.Professor.objects.all()[0]
        data = serializers.ProfessorSerializers(group).data
        self.assertEquals(data['phone'], '+79631859823')
    
    def test_department_field_content(self):
        group = models.Professor.objects.all()[0]
        data = serializers.ProfessorSerializers(group).data
        self.assertEquals(data['department'], 'ИИТК')


class PlaceSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Place.objects.create(name='Н317')

    def test_contains_expected_fields(self):
        fields = ['name','id']
        place = models.Place.objects.all()[0]
        data = serializers.PlaceSerializers(place).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_name_field_content(self):
        place = models.Place.objects.all()[0]
        data = serializers.PlaceSerializers(place).data
        self.assertEquals(data['name'], 'Н317')


class SubjectSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Subject.objects.create(
            title='Физкультура',
            type=1
        )

    def test_contains_expected_fields(self):
        fields = ['id', 'title', 'type']
        subject = models.Subject.objects.all()[0]
        data = serializers.SubjectSerializers(subject).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_title_field_content(self):
        subject = models.Subject.objects.all()[0]
        data = serializers.SubjectSerializers(subject).data
        self.assertEquals(data['title'], 'Физкультура')

    def test_type_field_content(self):
        subject = models.Subject.objects.all()[0]
        data = serializers.SubjectSerializers(subject).data
        self.assertEquals(data['type'], 1)


class SubgroupSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Subgroup.objects.create(
            place=models.Place.objects.create(name='Н317'),
            subject=models.Subject.objects.create(title='Физкультура', type=1)
        )

    def test_contains_expected_fields(self):
        fields = ['num', 'subject', 'type', 'place', 'groups', 'professors']
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_num_field_content(self):
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(data['num'], 0)

    def test_subject_field_content(self):
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(data['subject'], 'Физкультура')

    def test_type_field_content(self):
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(data['type'], 1)

    def test_groups_field_content(self):
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(data['groups'], [])

    def test_professors_field_content(self):
        supgroup = models.Subgroup.objects.all()[0]
        data = serializers.SubgroupSerializers(supgroup).data
        self.assertEquals(data['professors'], [])


class LessonSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Lesson.objects.create(time='13:00-14:30')

    def test_contains_expected_fields(self):
        fields = ['subgroups', 'time']
        lesson = models.Lesson.objects.all()[0]
        data = serializers.LessonSerializers(lesson).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_subgroups_field_content(self):
        lesson = models.Lesson.objects.all()[0]
        data = serializers.LessonSerializers(lesson).data
        self.assertEquals(data['subgroups'], [])

    def test_time_field_content(self):
        lesson = models.Lesson.objects.all()[0]
        data = serializers.LessonSerializers(lesson).data
        self.assertEquals(data['time'], '13:00-14:30')


class GroupTimetableSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetableGroup.objects.create(
            even_week=True,
            day=0,
            group=models.Group.objects.create(name='БПИ18-01')
        )

    def test_contains_expected_fields(self):
        fields = ['day', 'lesson']
        time_table = models.TimetableGroup.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_day_field_content(self):
        time_table = models.TimetableGroup.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['day'], 0)

    def test_lesson_field_content(self):
        time_table = models.TimetableGroup.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['lesson'], [])


class PlaceTimetableSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetablePlace.objects.create(
            even_week=True,
            day=0,
            place=models.Place.objects.create(name='Н317')
        )

    def test_contains_expected_fields(self):
        fields = ['day', 'lesson']
        time_table = models.TimetablePlace.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_day_field_content(self):
        time_table = models.TimetablePlace.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['day'], 0)

    def test_lesson_field_content(self):
        time_table = models.TimetablePlace.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['lesson'], [])


class ProfessorTimetableSerializersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetableProfessor.objects.create(
            even_week=True,
            day=0,
            professor=models.Professor.objects.create(name='ФИО')
        )

    def test_contains_expected_fields(self):
        fields = ['day', 'lesson']
        time_table = models.TimetableProfessor.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(set(data.keys()), set(fields))

    def test_day_field_content(self):
        time_table = models.TimetableProfessor.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['day'], 0)

    def test_lesson_field_content(self):
        time_table = models.TimetableProfessor.objects.all()[0]
        data = serializers.TimetableSerializers(time_table).data
        self.assertEquals(data['lesson'], [])