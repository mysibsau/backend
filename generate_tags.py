from apps.timetable.models import Lesson, Tag
from re import sub
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
allowed_postags = {'NOUN', 'ADJF', 'VERB', 'ADVB'}

lessons = [lesson.name_ru.lower() for lesson in Lesson.objects.all()]
lessons = [lesson.replace('-', ' ') for lesson in lessons]
lessons = [lesson.replace('.', '') for lesson in lessons]
lessons = [lesson.replace(',', '') for lesson in lessons]
lessons = [sub(r'\([^)]*\)', '', lesson) for lesson in lessons]
words = []
for lesson in lessons:
    words += lesson.split(' ')
print(len(words))
words = [word for word in words if len(word) >= 3]
words = [word for word in words if morph.parse(word)[0].tag.POS in allowed_postags]
count_words = {word: words.count(word) for word in words if words.count(word) > 10}
words_normailze = {word: morph.parse(word)[0].normal_form for word in count_words.keys()}
print(set(words_normailze.values()))