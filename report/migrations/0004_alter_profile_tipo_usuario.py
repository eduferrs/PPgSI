# Generated by Django 5.1.2 on 2024-10-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_profile_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tipo_usuario',
            field=models.CharField(choices=[('aluno', 'Aluno'), ('coordenador', 'Coordenador'), ('orientador', 'Orientador')], max_length=12),
        ),
    ]
