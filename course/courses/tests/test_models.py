from django.test import TestCase

from courses.models import Course, Category


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test_category_name', imgpath='test_category_imgpath')
        Course.objects.create(name='test_name', description='test_desc', category=test_category, logo='test_path')

    def test_name(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_desc(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_logo(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('logo').verbose_name
        self.assertEqual(field_label, 'logo')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        m_l = course._meta.get_field('name').max_length
        self.assertEqual(m_l, 122)

    def test_desc_max_length(self):
        course = Course.objects.get(id=1)
        m_l = course._meta.get_field('description').max_length
        self.assertEqual(m_l, 255)

    def test_logo_max_length(self):
        course = Course.objects.get(id=1)
        m_l = course._meta.get_field('logo').max_length
        self.assertEqual(m_l, 255)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Course._meta.verbose_name_plural), 'Courses')

# here is CategoryModelTest, ContactsModelTest and BranchModelTest classes
# believe me
