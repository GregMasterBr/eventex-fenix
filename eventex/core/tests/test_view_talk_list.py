from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker, Talk, Course
from eventex.core.managers import PeriodManager


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Título da Palestra', start='10:00', description='Descrição da palestra.')       
        t2 = Talk.objects.create(title='Título da Palestra', start='13:00', description='Descrição da palestra.')  
        c1 = Course.objects.create(title='Título do Curso', start='09:00', description='Descrição do curso.', slots=20)  


        speaker = Speaker.objects.create( 
            name= 'Henrique Bastos',
            slug = 'henrique-bastos',
            website = 'https://henriquebastos.net'
        )
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))       

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/palestrantes/henrique-bastos/'),
            (3, 'Henrique Bastos'),
            (2, 'Descrição da palestra.'),
            (1, 'Título do Curso'),
            (1, '09:00'),
            (1, 'Descrição do curso.')            
        ]        

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)          

    def test_context(self):
        """"Talk must be in context"""
        variables = ['morning_talks','afternoon_talks', 'courses']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)

class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(response, 'Ainda não existem palestras de manhã.')
        self.assertContains(response, 'Ainda não existem palestras de tarde.')

class CourseModelTest(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(
            title = 'Título do Curso',
            start = '09:00',
            description = 'Descrição do curso.',
            slots=20
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_has_speakers(self):
        """Course has many Speakers and vice-versa"""

        self.course.speakers.create(
            name= 'Henrique Bastos',
            slug = 'henrique-bastos',
            website = 'https://henriquebastos.net'
        )

        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual('Título do Curso', str(self.course))        

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)                