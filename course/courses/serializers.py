from rest_framework import serializers

from courses.models import Course, Category, Branch, Contact

class ContactSerializers(serializers.ModelSerializer):
    contact_choice = serializers.SerializerMethodField()
    class Meta:
        model = Contact
        fields = ('contact_choice', 'value',)

    def get_contact_choice(self, obj):
        return obj.get_contact_choice_display()





class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address',)


class CategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = ('name',)


class CourseSerializer(serializers.ModelSerializer):

    contacts = ContactSerializers(many=True, required=False)
    branches = BranchSerializer(many=True, required=False)
    category = CategorySerializers()

    class Meta:
        model = Course
        fields = ("id", "name", "description", "logo", "category", "contacts", "branches")

    def create(self, validated_data):
        categ_data = validated_data.pop('category')
        cont_data = validated_data.pop('contacts')
        bran_data = validated_data.pop('branches')
        categ_value = categ_data['name']
        course = Course.objects.create(**validated_data, category=Category.objects.get(name=categ_value))
        for contact in cont_data:
            Contact.objects.create(course=course, **contact)
        for branch in bran_data:
            Branch.objects.create(course=course, **branch)
        return course


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.branches = validated_data.get('branches', instance.branches)
        instance.save()
        return instance
