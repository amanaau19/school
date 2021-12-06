# Generated by Django 3.2.9 on 2021-11-25 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_alter_course_max_students'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='/profile_images')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tutors', to='courses.course')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='employees.employee')),
            ],
        ),
    ]
