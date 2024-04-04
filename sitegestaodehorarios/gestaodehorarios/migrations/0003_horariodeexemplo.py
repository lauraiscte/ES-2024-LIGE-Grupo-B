# Generated by Django 4.2.11 on 2024-03-31 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaodehorarios', '0002_caracterizacaodassalas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horariodeexemplo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.TextField(blank=True, db_column='Curso', null=True)),
                ('unidade_curricular', models.TextField(blank=True, db_column='Unidade Curricular', null=True)),
                ('turno', models.TextField(blank=True, db_column='Turno', null=True)),
                ('turma', models.TextField(blank=True, db_column='Turma', null=True)),
                ('inscritos_no_turno', models.IntegerField(blank=True, db_column='Inscritos no turno', null=True)),
                ('dia_da_semana', models.TextField(blank=True, db_column='Dia da semana', null=True)),
                ('hora_inicio', models.TextField(blank=True, db_column='Hora início da aula', null=True)),
                ('hora_fim', models.TextField(blank=True, db_column='Hora fim da aula', null=True)),
                ('data_da_aula', models.TextField(blank=True, db_column='Data da aula', null=True)),
                ('caracteristicas_sala', models.TextField(blank=True, db_column='Características da sala pedida para a aula', null=True)),
                ('sala_atribuida', models.TextField(blank=True, db_column='Sala atribuída à aula', null=True)),
            ],
            options={
                'db_table': 'HorarioDeExemplo',
                'managed': False,
            },
        ),
    ]