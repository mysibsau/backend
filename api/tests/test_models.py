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
        group = models.Group.objects.get(id=1)
        for label in labels:
            object_label = group._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_object_name_is_group_name(self):
        group = models.Group.objects.get(id=1)
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
        professor = models.Professor.objects.get(id=1)
        for label in labels:
            object_label = professor._meta.get_field(label).verbose_name
            self.assertEquals(object_label, labels[label])

    def test_phone_max_length(self):
        professor = models.Professor.objects.get(id=1)
        max_length = professor._meta.get_field('phone').max_length
        self.assertEquals(max_length, 12)

    def test_object_name_is_professor_name(self):
        professor = models.Professor.objects.get(id=1)
        self.assertEquals(professor.name, str(professor))


class PlaceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Place.objects.create(
            title='Н317',
        )

    def test_labels(self):
        place = models.Place.objects.get(id=1)
        title_label = place._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'Название')

    def test_title_max_length(self):
        place = models.Place.objects.get(id=1)
        max_length = place._meta.get_field('title').max_length
        self.assertEquals(max_length, 10)

    def test_object_name_is_place_title(self):
        place = models.Place.objects.get(id=1)
        self.assertEquals(place.title, str(place))