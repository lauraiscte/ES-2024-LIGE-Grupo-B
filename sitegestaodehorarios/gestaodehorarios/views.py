import csv
import json
from datetime import datetime, time

from django.contrib import messages
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from gestaodehorarios.models import Caracterizacaodassalas, Horariodeexemplo


def index(request):
    return render(request, 'gestaodehorarios/index.html')


def carregar_dados_csv(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Iniciar uma transação em lote
        with transaction.atomic():
            objetos_criados = []
            for row in reader:
                data_aula_parts = row['Data da aula'].split('/')
                if len(data_aula_parts) == 3:
                    data_aula = datetime(int(data_aula_parts[2]), int(data_aula_parts[1]), int(data_aula_parts[0]))
                else:
                    data_aula = None
                hora_inicio = criar_data_com_string_de_hora(row['Hora inicio da aula'])
                hora_fim = criar_data_com_string_de_hora(row['Hora fim da aula'])
                semana_ano = get_semana_ano(data_aula) if data_aula else None
                semana_semestre = get_semana_semestre(data_aula) if data_aula else None

                objeto = Horariodeexemplo(
                    curso=row['Curso'],
                    unidade_curricular=row['Unidade Curricular'],
                    turno=row['Turno'],
                    turma=row['Turma'],
                    inscritos_no_turno=row['Inscritos no turno'],
                    dia_da_semana=row['Dia da semana'],
                    hora_inicio=hora_inicio.time(),
                    hora_fim=hora_fim.time(),
                    data_da_aula=data_aula.date() if data_aula else None,
                    caracteristicas_sala=row['Caracteristicas da sala pedida para a aula'],
                    sala_atribuida=row['Sala atribuida a aula'],
                    semanaAno=semana_ano,
                    semanaSemestre=semana_semestre
                )

                objetos_criados.append(objeto)

            # Realizar operação bulk_create para inserir todos os objetos de uma vez
            Horariodeexemplo.objects.bulk_create(objetos_criados)


def get_semana_ano(date):
    first_day_year = datetime(date.year, 1, 1)  # Criar objeto datetime para o primeiro dia do ano
    diff = date - first_day_year  # Calcular a diferença em dias entre as duas datas
    semana_ano = diff.days // 7 + 1  # Calcular o número da semana do ano
    return semana_ano


def get_semana_semestre(date):
    month = date.month  # Janeiro - 1, ...
    if month >= 9:  # De setembro a dezembro pertence ao 1º semestre
        first_day_semester = datetime(date.year, 9, 1)  # 1 de Setembro - Data do início do 1º semestre
    elif month < 2:  # Janeiro pertence ao 1º semestre do ano anterior
        first_day_semester = datetime(date.year - 1, 9,
                                      1)  # 1 de Setembro - Data do início do 1º semestre do ano anterior
    else:  # De fevereiro a agosto pertence ao 2º semestre
        first_day_semester = datetime(date.year, 2, 1)  # 1 de Fevereiro - Data do início do 2º semestre

    diff = date - first_day_semester
    semana_semestre = diff.days // 7 + 1
    return semana_semestre


def criar_data_com_string_de_hora(hora_string):
    # Dividir a string de hora em partes separadas
    partes_hora = hora_string.split(':')

    # Extrair horas, minutos e segundos
    horas = int(partes_hora[0])
    minutos = int(partes_hora[1])
    segundos = int(partes_hora[2])

    # Retornar um objeto datetime com a hora
    return datetime.now().replace(hour=horas, minute=minutos, second=segundos, microsecond=0)


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, time):
            return obj.strftime('%H:%M:%S')  # Convert time object to string
        return super().default(obj)


def processar_csv(request):
    if request.method == 'POST':
        if 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            # Salvar o arquivo temporariamente
            with open('temp.csv', 'wb') as temp_file:
                for chunk in csv_file.chunks():
                    temp_file.write(chunk)
            # Limpar dados antigos (se necessário)
            Horariodeexemplo.objects.all().delete()
            # Carregar novos dados
            carregar_dados_csv('temp.csv')
            # dados_para_tabela = obter_dados_horario()
            # dados_json = json.dumps(dados_para_tabela, cls=CustomJSONEncoder)
            return redirect('gestaodehorarios:pagina_horario')
        else:
            # Adicione uma mensagem de erro
            messages.error(request, 'Nenhum arquivo selecionado. Por favor, selecione um arquivo para enviar.')
            return render(request, 'gestaodehorarios/index.html')
    else:
        return render(request, 'gestaodehorarios/index.html')


def pagina_horario(request):
    dados_para_tabela = obter_dados_horario()
    dados_json = json.dumps(dados_para_tabela, cls=CustomJSONEncoder)
    return render(request, 'gestaodehorarios/horario.html', {'dados_para_tabela': dados_json})


def carregar_salas(request):
    dados_para_tabela = obter_dados_para_tabela()
    dados_json = json.dumps(dados_para_tabela)
    return render(request, 'gestaodehorarios/salas.html', {'dados_para_tabela': dados_json})


def obter_dados_para_tabela():
    # Consulta ao banco de dados para recuperar todos os objetos Caracterizacaodassalas
    dados_caracterizacao = Caracterizacaodassalas.objects.all()

    # Lista para armazenar os dados formatados
    dados_formatados = []

    # Iterar sobre cada objeto Caracterizacaodassalas e formatar os dados
    for caracterizacao in dados_caracterizacao:
        dados_formatados.append({
            "edificio": caracterizacao.edificio,
            "nomeSala": caracterizacao.nome_sala,
            "capacidadeNormal": caracterizacao.capacidade_normal,
            "capacidadeExame": caracterizacao.capacidade_exame,
            "numCaracteristicas": caracterizacao.n_caracteristicas,
            "anfiteatro": caracterizacao.anfiteatro_aulas,
            "apoioTecnicoEventos": caracterizacao.apoio_tecnico_eventos,
            "arq1": caracterizacao.arq_1,
            "arq2": caracterizacao.arq_2,
            "arq3": caracterizacao.arq_3,
            "arq4": caracterizacao.arq_4,
            "arq5": caracterizacao.arq_5,
            "arq6": caracterizacao.arq_6,
            "arq9": caracterizacao.arq_9,
            "byod": caracterizacao.byod,
            "focusGroup": caracterizacao.focus_group,
            "horarioVisivelPub": caracterizacao.horario_visivel_publico,
            "labArqI": caracterizacao.lab_arq_comp_i,
            "labArqII": caracterizacao.lab_arq_comp_ii,
            "labBasesEng": caracterizacao.lab_de_bases_de_engenharia,
            "labEletro": caracterizacao.lab_de_electro,
            "labInfo": caracterizacao.lab_de_informatica,
            "labJornalismo": caracterizacao.lab_de_jornalismo,
            "labRedesCompI": caracterizacao.lab_redes_de_comp_i,
            "labRedesCompII": caracterizacao.lab_redes_de_comp_ii,
            "labTele": caracterizacao.lab_de_tele,
            "salaAulasMestrado": caracterizacao.sala_aulas_mestrado,
            "salaAulasMestradoPlus": caracterizacao.sala_aulas_mestrado_plus,
            "salaNee": caracterizacao.sala_nee,
            "salaProvas": caracterizacao.sala_provas,
            "salaReuniao": caracterizacao.sala_reuniao,
            "salaArquitetura": caracterizacao.sala_de_arquitectura,
            "salaAulaNormal": caracterizacao.sala_de_aulas_normal,
            "videoconferencia": caracterizacao.videoconferencia,
            "atrio": caracterizacao.atrio,
        })

    return dados_formatados


def obter_dados_horario():
    # Consulta ao banco de dados para recuperar todos os objetos Horariodeexemplo
    dados_horario = Horariodeexemplo.objects.all()

    # Lista para armazenar os dados formatados
    dados_formatados = []

    # Iterar sobre cada objeto Caracterizacaodassalas e formatar os dados
    for horario in dados_horario:
        dados_formatados.append({
            "curso": horario.curso,
            "uc": horario.unidade_curricular,
            "turno": horario.turno,
            "turma": horario.turma,
            "inscritos": horario.inscritos_no_turno,
            "dia": horario.dia_da_semana,
            "horaInicio": horario.hora_inicio,
            "horaFim": horario.hora_fim,
            "data": horario.data_da_aula,
            "caracteristicas": horario.caracteristicas_sala,
            "sala": horario.sala_atribuida,
            "semanaAno": horario.semanaAno,
            "semanaSemestre": horario.semanaSemestre,
        })

    return dados_formatados


def verificar_salas(request):
    if request.method == 'POST':
        data = request.POST.get('Data')
        hora = request.POST.get('Hora')

        if data and hora:
            try:
                # Convertendo data e hora para datetime
                data_hora = datetime.strptime(data + ' ' + hora, '%Y-%m-%d %H:%M')

                # Verificar se há aula agendada na data e hora específicas
                aulas_agendadas = Horariodeexemplo.objects.filter(data_da_aula=data_hora.date(),
                                                                  hora_inicio__lte=data_hora.time(),
                                                                  hora_fim__gt=data_hora.time())

                if aulas_agendadas.exists():
                    # Se houver aula, retornar as salas disponíveis
                    salas_ocupadas = [aula.sala_atribuida for aula in aulas_agendadas]
                    salas_disponiveis = Caracterizacaodassalas.objects.exclude(nome_sala__in=salas_ocupadas)

                    # Serializando os objetos Caracterizacaodassalas
                    salas_disponiveis_serialized = []
                    for sala in salas_disponiveis:
                        serialized_sala = {
                            "edificio": sala.edificio,
                            "nomeSala": sala.nome_sala,
                            "capacidadeNormal": sala.capacidade_normal,
                            "capacidadeExame": sala.capacidade_exame,
                            "numCaracteristicas": sala.n_caracteristicas,
                            "anfiteatro": sala.anfiteatro_aulas,
                            "apoioTecnicoEventos": sala.apoio_tecnico_eventos,
                            "arq1": sala.arq_1,
                            "arq2": sala.arq_2,
                            "arq3": sala.arq_3,
                            "arq4": sala.arq_4,
                            "arq5": sala.arq_5,
                            "arq6": sala.arq_6,
                            "arq9": sala.arq_9,
                            "byod": sala.byod,
                            "focusGroup": sala.focus_group,
                            "horarioVisivelPub": sala.horario_visivel_publico,
                            "labArqI": sala.lab_arq_comp_i,
                            "labArqII": sala.lab_arq_comp_ii,
                            "labBasesEng": sala.lab_de_bases_de_engenharia,
                            "labEletro": sala.lab_de_electro,
                            "labInfo": sala.lab_de_informatica,
                            "labJornalismo": sala.lab_de_jornalismo,
                            "labRedesCompI": sala.lab_redes_de_comp_i,
                            "labRedesCompII": sala.lab_redes_de_comp_ii,
                            "labTele": sala.lab_de_tele,
                            "salaAulasMestrado": sala.sala_aulas_mestrado,
                            "salaAulasMestradoPlus": sala.sala_aulas_mestrado_plus,
                            "salaNee": sala.sala_nee,
                            "salaProvas": sala.sala_provas,
                            "salaReuniao": sala.sala_reuniao,
                            "salaArquitetura": sala.sala_de_arquitectura,
                            "salaAulaNormal": sala.sala_de_aulas_normal,
                            "videoconferencia": sala.videoconferencia,
                            "atrio": sala.atrio
                        }
                        salas_disponiveis_serialized.append(serialized_sala)

                    salas_disponiveis_json = json.dumps(salas_disponiveis_serialized)

                    return render(request, 'gestaodehorarios/salas.html',
                                  {'dados_para_tabela': salas_disponiveis_json})
                else:
                    # Se não houver aula, todas as salas estão disponíveis
                    salas_disponiveis = Caracterizacaodassalas.objects.all()

                    # Serializando os objetos Caracterizacaodassalas
                    salas_disponiveis_serialized = serialize('json', salas_disponiveis)

                    return render(request, 'gestaodehorarios/salas.html',
                                  {'dados_para_tabela': salas_disponiveis_serialized})
            except ValueError:
                return JsonResponse({'error': 'Formato de data ou hora inválido.'})
        else:
            return JsonResponse({'error': 'Data e hora são obrigatórias.'})
    else:
        return JsonResponse({'error': 'Método não suportado.'})

