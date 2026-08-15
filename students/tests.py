from django.test import TestCase, Client
from django.urls import reverse
from .models import Student
from .forms import StudentForm


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Alice Smith",
            age=20,
            student_class="CS-101",
            roll_no=101,
            marks=92
        )

    def test_student_str(self):
        self.assertEqual(str(self.student), "Alice Smith")


class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(
            name="Bob Jones",
            age=22,
            student_class="EE-201",
            roll_no=102,
            marks=85
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob Jones")

    def test_student_list_search_filter(self):
        response = self.client.get(reverse('student_list'), {'search_name': 'Bob'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob Jones")

        response_invalid = self.client.get(reverse('student_list'), {'search_age': 'invalid_age'})
        self.assertEqual(response_invalid.status_code, 200)

    def test_student_create_view(self):
        response = self.client.post(reverse('student_create'), {
            'name': 'Charlie Brown',
            'age': 19,
            'student_class': 'ME-301',
            'roll_no': 103,
            'marks': 78
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(roll_no=103).exists())

    def test_student_update_view(self):
        response = self.client.post(reverse('student_update', kwargs={'pk': self.student.pk}), {
            'name': 'Bob Updated',
            'age': 23,
            'student_class': 'EE-201',
            'roll_no': 102,
            'marks': 90
        })
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Bob Updated')

    def test_student_delete_view(self):
        response = self.client.post(reverse('student_delete', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())


class StudentAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(
            name="David Lee",
            age=21,
            student_class="CS-102",
            roll_no=104,
            marks=88
        )

    def test_api_student_list(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "David Lee")
