# Generated by Django 5.1.2 on 2024-11-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_relatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='nusp',
            field=models.CharField(max_length=11),
        ),
    ]
