from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey("schools_app.School", on_delete=models.PROTECT, related_name="departments")

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    date_of_birth = models.DateField()
    image = models.ImageField("/profile_images", null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=7, decimal_places=2)


class Tutor(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="tutor")
    experience = models.PositiveSmallIntegerField()
    course = models.ForeignKey("courses.Course", on_delete=models.PROTECT, related_name="tutors")


# def user_created(sender, instance, **kwargs):
#     Token.objcets.create(user=instance)
#
#
# post_save.connect(user_created, sender=User)
