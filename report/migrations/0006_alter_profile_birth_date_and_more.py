# Generated by Django 5.1.2 on 2024-11-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_profile_advisor_profile_birth_date_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='enrollment_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='exam_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language_exam_date',
            field=models.DateField(blank=True),
        ),
    ]
