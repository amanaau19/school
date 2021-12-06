from rest_framework import serializers
from .models import Course
from schools_app.models import School


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    is_active = serializers.BooleanField(default=False)
    price = serializers.DecimalField(max_digits=14, decimal_places=2)
    duration = serializers.IntegerField(min_value=1, max_value=9)
    max_students = serializers.IntegerField(min_value=1, max_value=20)

    def validate(self, attrs):
        name = attrs["name"]
        school = attrs["school"]
        course = Course.objects.filter(name=name, school=school).exists()
        if course:
            raise serializers.ValidationError(
                detail="Course name must be unique",
                code="course_name_unique"
            )

        return super().validate(attrs)

    def create(self, validated_data):
        """create() method creates and returns a new Course instance"""
        course = Course.objects.create(**validated_data)
        return course

    def update(self, instance, validated_data):
        """
            Update and return existing instance
        """
        instance.name = validated_data.get("name", instance.name)
        instance.school = validated_data.get("school", instance.school)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.price = validated_data.get("price", instance.price)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.max_students = validated_data.get("max_students", instance.max_students)
        instance.save()
        return instance

