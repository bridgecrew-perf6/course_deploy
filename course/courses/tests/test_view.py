from django.test import TestCase

from rest_framework.reverse import reverse


class CourseViewTest(TestCase):

    def test_home_view(self):
        result = self.client.get(reverse('home'))
        self.assertEqual(result.status_code, 200)

    def test_home_is_used(self):
        result = self.client.get(reverse('home'))
        self.assertTemplateUsed(result, 'courses/home.html')
