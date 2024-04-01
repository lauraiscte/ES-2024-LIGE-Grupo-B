
//var tabledata = []; // Inicializa a variável tabledata
var table;

// Função para inicializar a tabela Tabulator
function iniciarTabelaSalas(dados_para_tabela) {
    // Inicializar a tabela Tabulator
    var table = new Tabulator("#example-table", {
        data: dados_para_tabela,
        layout: "fitDataFill",
        pagination: "local",
        paginationSize: 10,
        paginationSizeSelector: [5, 10, 20, 40],
        movableColumns: true,
        columns: [
            { title: "Edifício", field: "edificio", headerFilter: "input" },
            { title: "Nome Sala", field: "nomeSala", headerFilter: "input" },
            { title: "Capacidade Normal", field: "capacidadeNormal", headerFilter: "input" },
            { title: "Capacidade Exame", field: "capacidadeExame", headerFilter: "input" },
            { title: "Nº Características", field: "numCaracteristicas", headerFilter: "input" },
            { title: "Anfiteatro Aulas", field: "anfiteatro", headerFilter: "input" },
            { title: "Apoio Técnico Eventos", field: "apoioTecnicoEventos", headerFilter: "input" },
            { title: "Arq 1", field: "arq1", headerFilter: "input" },
            { title: "Arq 2", field: "arq2", headerFilter: "input" },
            { title: "Arq 3", field: "arq3", headerFilter: "input" },
            { title: "Arq 4", field: "arq4", headerFilter: "input" },
            { title: "Arq 5", field: "arq5", headerFilter: "input" },
            { title: "Arq 6", field: "arq6", headerFilter: "input" },
            { title: "Arq 9", field: "arq9", headerFilter: "input" },
            { title: "BYOD (Bring Your Own Device)", field: "byod", headerFilter: "input" },
            { title: "Focus Group", field: "focusGroup", headerFilter: "input" },
            { title: "Horário Sala Visível Portal Público", field: "horarioVisivelPub", headerFilter: "input" },
            { title: "Laboratório de Arquitectura de Computadores I", field: "labArqI", headerFilter: "input" },
            { title: "Laboratório de Arquitectura de Computadores II", field: "labArqII", headerFilter: "input" },
            { title: "Laboratório de Bases de Engenharia", field: "labBasesEng", headerFilter: "input" },
            { title: "Laboratório de Electrónica", field: "labEletro", headerFilter: "input" },
            { title: "Laboratório de Informática", field: "labInfo", headerFilter: "input" },
            { title: "Laboratório de Jornalismo", field: "labJornalismo", headerFilter: "input" },
            { title: "Laboratório de Redes de Computadores I", field: "labRedesCompI", headerFilter: "input" },
            { title: "Laboratório de Redes de Computadores II", field: "labRedesCompII", headerFilter: "input" },
            { title: "Laboratório de Telecomunicações", field: "labTele", headerFilter: "input" },
            { title: "Sala Aulas Mestrado", field: "salaAulasMestrado", headerFilter: "input" },
            { title: "Sala Aulas Mestrado Plus", field: "salaAulasMestradoPlus", headerFilter: "input" },
            { title: "Sala NEE", field: "salaNee", headerFilter: "input" },
            { title: "Sala Provas", field: "salaProvas", headerFilter: "input" },
            { title: "Sala Reunião", field: "salaReuniao", headerFilter: "input" },
            { title: "Sala de Arquitectura", field: "salaArquitetura", headerFilter: "input" },
            { title: "Sala de Aulas Normal", field: "salaAulaNormal", headerFilter: "input" },
            { title: "Videoconferência", field: "videoconferencia", headerFilter: "input" },
            { title: "Átrio", field: "atrio", headerFilter: "input" },
        ],
    });

    // Adiciona um listener para as caixas de seleção
    var checkboxes = document.querySelectorAll('input[type=checkbox][name=column]');
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            var column = this.value;
            var visible = this.checked;
            table.toggleColumn(column, visible);
        });
    });
}



