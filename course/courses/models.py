from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=152)
    imgpath = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length = 122)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name = 'Courses', null = True, on_delete = models.CASCADE)
    logo = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length = 255)
    longitude = models.CharField(max_length = 1020)
    address = models.CharField(max_length = 122)
    course = models.ForeignKey(Course, related_name = 'Branches', null = True, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.address



class Contact(models.Model):
    contact_choices = ((1, 'Phone'), (2, 'Facebook'), (3, 'Email'))
    contact_choice = models.IntegerField(choices = contact_choices, default = 1)
    value = models.CharField(max_length = 122)
    course = models.ForeignKey(Course, related_name = 'Contacts', null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.value
