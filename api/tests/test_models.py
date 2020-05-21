from django.test import TestCase
import api.models as models

class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Group.objects.create(
            name='БПИ18-01',
            mail='test@sibsau.ru'
        )

    def test_labels(self):
        labels = {
            'name': 'Название',
            'mail': 'Почта'
        }
        group = models.Group.objects.all()[0]
        for label in labels:
            object_label = group._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_object_name_is_group_name(self):
        group = models.Group.objects.all()[0]
        self.assertEquals(group.name, str(group))


class ProfessorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Professor.objects.create(
            name='Фамилия Имя Отчество',
            mail='fio@sibsau.ru',
            phone='+79631859823',
            department = 'ИИТК'
        )

    def test_labels(self):
        labels = {
            'name': 'ФИО',
            'mail': 'Почта',
            'phone': 'Телефон',
            'department': 'Кафедра'
        }
        professor = models.Professor.objects.all()[0]
        for label in labels:
            object_label = professor._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_phone_max_length(self):
        professor = models.Professor.objects.all()[0]
        max_length = professor._meta.get_field('phone').max_length
        self.assertEquals(max_length, 12)

    def test_object_name_is_professor_name(self):
        professor = models.Professor.objects.all()[0]
        self.assertEquals(professor.name, str(professor))


class PlaceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Place.objects.create(title='Н317')

    def test_labels(self):
        place = models.Place.objects.all()[0]
        title_label = place._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'Название')

    def test_title_max_length(self):
        place = models.Place.objects.all()[0]
        max_length = place._meta.get_field('title').max_length
        self.assertEquals(max_length, 10)

    def test_object_name_is_place_title(self):
        place = models.Place.objects.all()[0]
        self.assertEquals(place.title, str(place))


class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Subject.objects.create(
            title='Физкультура',
            type=1
        )

    def test_labels(self):
        labels = {
            'title': 'Название',
            'type': 'Тип'
        }
        subject = models.Subject.objects.all()[0]
        for label in labels:
            object_label = subject._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_object_name_is_subject_title(self):
        subject = models.Subject.objects.all()[0]
        self.assertEquals(subject.title, str(subject))


class SubgroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Subgroup.objects.create(
            place=models.Place.objects.create(title='Н317'),
            subject=models.Subject.objects.create(title='Физкультура', type=1)
        )

    def test_labels(self):
        labels = {
            'professors': 'Преподаватели',
            'groups': 'Группы',
            'place': 'Аудитория',
            'subject': 'Предмет',
            'num': 'Подгруппа'
        }
        subgroup = models.Subgroup.objects.all()[0]
        for label in labels:
            object_label = subgroup._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_object_name_is_subject_title(self):
        subgroup = models.Subgroup.objects.all()[0]
        self.assertEquals(subgroup.subject.title, str(subgroup.subject))


class LessonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Lesson.objects.create(time='13:00-14:30')

    def test_labels(self):
        labels = {
            'time': 'Время',
            'subgroup': 'Предметы',
        }
        lesson = models.Lesson.objects.all()[0]
        for label in labels:
            object_label = lesson._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_time_max_length(self):
        lesson = models.Lesson.objects.all()[0]
        max_length = lesson._meta.get_field('time').max_length
        self.assertEquals(max_length, 11)


class TimetableGroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetableGroup.objects.create(
            even_week=True,
            day=0,
            group=models.Group.objects.create(name='БПИ18-01')
        )

    def test_labels(self):
        labels = {
            'even_week': 'Четная неделя',
            'day': 'День недели',
            'lesson': 'Ленты',
            'group': 'Группа',
        }
        timtable = models.TimetableGroup.objects.all()[0]
        for label in labels:
            object_label = timtable._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])


class TimetablePlaceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetablePlace.objects.create(
            even_week=True,
            day=0,
            place=models.Place.objects.create(title='Н317')
        )

    def test_labels(self):
        labels = {
            'even_week': 'Четная неделя',
            'day': 'День недели',
            'lesson': 'Ленты',
            'place': 'Кабинет',
        }
        timtable = models.TimetablePlace.objects.all()[0]
        for label in labels:
            object_label = timtable._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])


class TimetableProfessorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.TimetableProfessor.objects.create(
            even_week=True,
            day=0,
            professor=models.Professor.objects.create(name='ФИО')
        )

    def test_labels(self):
        labels = {
            'even_week': 'Четная неделя',
            'day': 'День недели',
            'lesson': 'Ленты',
            'professor': 'Преподаватель',
        }
        timtable = models.TimetableProfessor.objects.all()[0]
        for label in labels:
            object_label = timtable._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])