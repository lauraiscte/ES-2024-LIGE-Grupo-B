/**
 * 
 */

var tabledata = []; // Inicializa a variável tabledata
var table;

//     document.getElementById('fileInput').addEventListener('change', handleFileSelect, false);

//     // Função para ler o arquivo CSV
//     function handleFileSelect(event) {
//         var file = event.target.files[0];
//         var reader = new FileReader();
//         reader.onload = function(e) {
//             var contents = e.target.result;
//             lerCSV(contents);
//         };
//         reader.readAsText(file);
//     }

function lerCSV(csv) {
	
	fetch(csv)
    .then(response => response.text())
    .then(text => {
        var lines = text.trim().split('\n');
        lines.shift(); // Remove o cabeçalho
    
    lines.forEach(function(line) {
        var columns = line.split(';');           
        
        tabledata.push({
            edificio: columns[0],
            nomeSala: columns[1],
            capacidadeNormal: columns[2],
            capacidadeExame: columns[3],
            numCaracteristicas: columns[4],
            anfiteatro: columns[5],
            apoioTecnicoEventos: columns[6],
            arq1: columns[7],
            arq2: columns[8],
            arq3: columns[9],
            arq4: columns[10],
            arq5: columns[11],
            arq6: columns[12],
            arq9: columns[13],
            byod: columns[14],
            focusGroup: columns[15],
            horarioVisivelPub: columns[16],
            labArqI: columns[17],
            labArqII: columns[18],
            labBasesEng: columns[19],
            labEletro: columns[20],
            labInfo: columns[21],
            labJornalismo: columns[22],
            labRedesCompI: columns[23],
            labRedesCompII: columns[24],
            labTele: columns[25],
            salaAulasMestrado: columns[26],
            salaAulasMestradoPlus: columns[27],
            salaNee: columns[28],
            salaProvas: columns[29],
            salaReuniao: columns[30],
            salaArquitetura: columns[31],
            salaAulaNormal: columns[32],
            videoconferencia: columns[33],
            atrio: columns[34],            
        });

    });
    // Inicializa a tabela Tabulator com os dados lidos
    iniciarTabela();
    })
    .catch(error => console.error(error));
}

// Função para inicializar a tabela Tabulator
function iniciarTabela() {
    table = new Tabulator("#example-table", {
        data: tabledata,
        layout: "fitDatafill",
        pagination: "local",
        paginationSize: 10,
        paginationSizeSelector: [5, 10, 20, 40],
        movableColumns: true,
        paginationCounter: "rows",
        initialSort: [{ column: "curso", dir: "asc" }],
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
    
lerCSV('CaracterizacaoDasSalas.csv');

function voltar() {
    history.back();
}