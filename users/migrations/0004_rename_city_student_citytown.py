# Generated by Django 4.2 on 2024-01-12 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_student_address_student_city_student_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='city',
            new_name='citytown',
        ),
    ]
