# Generated by Django 3.2.9 on 2021-11-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='/profile_images'),
        ),
    ]
