from django.db import models


# Create your models here.
class Aula(models.Model):
    curso = models.CharField(max_length=100)
    uc = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)
    inscritos = models.IntegerField()
    dia = models.DateField()
    horaInicio = models.TimeField()
    horaFim = models.TimeField()
    data = models.DateField()
    caracteristicas = models.CharField(max_length=255)
    sala = models.CharField(max_length=100)
    semanaAno = models.IntegerField()
    semanaSemestre = models.IntegerField()


class Sala(models.Model):
    edificio = models.CharField(max_length=100)
    nomeSala = models.CharField(max_length=100)
    capacidadeNormal = models.IntegerField()
    capacidadeExame = models.IntegerField()
    numCaracteristicas = models.IntegerField()
    anfiteatro = models.BooleanField()
    apoioTecnicoEventos = models.BooleanField()
    arq1 = models.BooleanField()
    arq2 = models.BooleanField()
    arq3 = models.BooleanField()
    arq4 = models.BooleanField()
    arq5 = models.BooleanField()
    arq6 = models.BooleanField()
    arq9 = models.BooleanField()
    byod = models.BooleanField()
    focusGroup = models.BooleanField()
    horarioVisivelPub = models.BooleanField()
    labArqI = models.BooleanField()
    labArqII = models.BooleanField()
    labBasesEng = models.BooleanField()
    labEletro = models.BooleanField()
    labInfo = models.BooleanField()
    labJornalismo = models.BooleanField()
    labRedesCompI = models.BooleanField()
    labRedesCompII = models.BooleanField()
    labTele = models.BooleanField()
    salaAulasMestrado = models.BooleanField()
    salaAulasMestradoPlus = models.BooleanField()
    salaNee = models.BooleanField()
    salaProvas = models.BooleanField()
    salaReuniao = models.BooleanField()
    salaArquitetura = models.BooleanField()
    salaAulaNormal = models.BooleanField()
    videoconferencia = models.BooleanField()
    atrio = models.BooleanField()


class Horariodeexemplo(models.Model):
    curso = models.TextField(db_column='Curso', blank=True, null=True)
    unidade_curricular = models.TextField(db_column='Unidade Curricular', blank=True, null=True)
    turno = models.TextField(db_column='Turno', blank=True, null=True)
    turma = models.TextField(db_column='Turma', blank=True, null=True)
    inscritos_no_turno = models.IntegerField(db_column='Inscritos no turno', blank=True, null=True)
    dia_da_semana = models.TextField(db_column='Dia da semana', blank=True, null=True)
    hora_inicio = models.TimeField(db_column='Hora inicio da aula', blank=True, null=True)
    hora_fim = models.TimeField(db_column='Hora fim da aula', blank=True, null=True)
    data_da_aula = models.DateField(db_column='Data da aula', blank=True, null=True)
    caracteristicas_sala = models.TextField(db_column='Caracteristicas da sala pedida para a aula', blank=True, null=True)
    sala_atribuida = models.TextField(db_column='Sala atribuida a aula', blank=True, null=True)
    semanaAno = models.IntegerField(db_column='Semana Ano', blank=True, null=True)
    semanaSemestre = models.IntegerField(db_column='Semana Semestre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HorarioDeExemplo'


class Caracterizacaodassalas(models.Model):
    edificio = models.TextField(db_column='Edifício', blank=True, null=True)
    nome_sala = models.TextField(db_column='Nome sala', blank=True, null=True)
    capacidade_normal = models.IntegerField(db_column='Capacidade Normal', blank=True, null=True)
    capacidade_exame = models.IntegerField(db_column='Capacidade Exame', blank=True, null=True)
    n_caracteristicas = models.IntegerField(db_column='Nº características', blank=True, null=True)
    anfiteatro_aulas = models.TextField(db_column='Anfiteatro aulas', blank=True, null=True)
    apoio_tecnico_eventos = models.TextField(db_column='Apoio técnico eventos', blank=True, null=True)
    arq_1 = models.TextField(db_column='Arq 1', blank=True, null=True)
    arq_2 = models.TextField(db_column='Arq 2', blank=True, null=True)
    arq_3 = models.TextField(db_column='Arq 3', blank=True, null=True)
    arq_4 = models.TextField(db_column='Arq 4', blank=True, null=True)
    arq_5 = models.TextField(db_column='Arq 5', blank=True, null=True)
    arq_6 = models.TextField(db_column='Arq 6', blank=True, null=True)
    arq_9 = models.TextField(db_column='Arq 9', blank=True, null=True)
    byod = models.TextField(db_column='BYOD (Bring Your Own Device)', blank=True, null=True)
    focus_group = models.TextField(db_column='Focus Group', blank=True, null=True)
    horario_visivel_publico = models.TextField(db_column='Horário sala visível portal público', blank=True, null=True)
    lab_arq_comp_i = models.TextField(db_column='Laboratório de Arquitectura de Computadores I', blank=True, null=True)
    lab_arq_comp_ii = models.TextField(db_column='Laboratório de Arquitectura de Computadores II', blank=True, null=True)
    lab_de_bases_de_engenharia = models.TextField(db_column='Laboratório de Bases de Engenharia', blank=True, null=True)
    lab_de_electro = models.TextField(db_column='Laboratório de Electrónica', blank=True, null=True)
    lab_de_informatica = models.TextField(db_column='Laboratório de Informática', blank=True, null=True)
    lab_de_jornalismo = models.TextField(db_column='Laboratório de Jornalismo', blank=True, null=True)
    lab_redes_de_comp_i = models.TextField(db_column='Laboratório de Redes de Computadores I', blank=True, null=True)
    lab_redes_de_comp_ii = models.TextField(db_column='Laboratório de Redes de Computadores II', blank=True, null=True)
    lab_de_tele = models.TextField(db_column='Laboratório de Telecomunicações', blank=True, null=True)
    sala_aulas_mestrado = models.TextField(db_column='Sala Aulas Mestrado', blank=True, null=True)
    sala_aulas_mestrado_plus = models.TextField(db_column='Sala Aulas Mestrado Plus', blank=True, null=True)
    sala_nee = models.TextField(db_column='Sala NEE', blank=True, null=True)
    sala_provas = models.TextField(db_column='Sala Provas', blank=True, null=True)
    sala_reuniao = models.TextField(db_column='Sala Reunião', blank=True, null=True)
    sala_de_arquitectura = models.TextField(db_column='Sala de Arquitectura', blank=True, null=True)
    sala_de_aulas_normal = models.TextField(db_column='Sala de Aulas normal', blank=True, null=True)
    videoconferencia = models.TextField(db_column='videoconferência', blank=True, null=True)
    atrio = models.TextField(db_column='Átrio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaracterizacaoDasSalas'