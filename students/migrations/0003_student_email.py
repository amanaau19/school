# Generated by Django 3.2.9 on 2021-12-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentcourse_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
