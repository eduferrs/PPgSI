# Generated by Django 5.1.2 on 2024-11-18 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_profile_failed_courses_profile_passed_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('nome_aluno', models.CharField(max_length=250)),
                ('nome_orientador', models.CharField(max_length=250)),
                ('lattes', models.URLField()),
                ('data_atualizacao_lattes', models.DateField()),
                ('curso', models.CharField(max_length=9)),
                ('data_matricula', models.DateField()),
                ('avaliacao_ultimo_relatorio', models.CharField(choices=[('Aprovado', 'Aprovado'), ('Aprovado com ressalvas', 'Aprovado com ressalvas'), ('Insatisfatório', 'Insatisfatório'), ('Não se aplica (é o primeiro relatório)', 'Não se aplica (é o primeiro relatório)')], max_length=38)),
                ('aporvacoes_inicio_curso', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('reprovacoes_semestre_anterior', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('reprovacoes_inicio_curso', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('realizacao_exame_idiomas', models.CharField(choices=[('Sim. Fui aprovado', 'Sim. Fui aprovado'), ('Sim. Fui reprovado', 'Sim. Fui reprovado'), ('Não', 'Não')], max_length=18)),
                ('realizacao_exame_qualificacao', models.CharField(choices=[('Sim. Fui aprovado', 'Sim. Fui aprovado'), ('Sim. Fui reprovado', 'Sim. Fui reprovado'), ('Não', 'Não')], max_length=18)),
                ('prazo_qualificacao', models.DateField(blank=True, null=True)),
                ('prazo_dissertacao', models.DateField()),
                ('artigos_em_escrita', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('artigos_em_avaliacao', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('artigos_publicados', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 ou mais', '4 ou mais')], max_length=9)),
                ('atividades_academicas_semestre_atual', models.TextField()),
                ('atividades_pesquisa', models.TextField()),
                ('declaracao_adicional', models.TextField(blank=True, null=True)),
                ('precisa_apoio', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3)),
                ('data_criacao', models.DateField()),
                ('parecer_orientador', models.CharField(blank=True, max_length=22, null=True)),
                ('parecer_coordenador', models.CharField(blank=True, max_length=22, null=True)),
                ('primeira_avaliacao', models.BooleanField(default=True)),
                ('nusp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.profile')),
            ],
        ),
    ]