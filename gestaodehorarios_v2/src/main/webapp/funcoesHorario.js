/**
 * 
 */
var tabledata = []; // Inicializa a variável tabledata
var table;
var salasOcupadas = []; // Armazenará os dados das salas ocupadas
var salasExistentes = []; // Armazenará os dados das salas existentes

//document.getElementById('fileInput').addEventListener('change', handleFileSelect, false);

function criarDataComStringDeHora(horaString) {
    // Dividir a string de hora em partes separadas
    var partesHora = horaString.split(':');

    // Extrair horas, minutos e segundos
    var horas = parseInt(partesHora[0], 10);
    var minutos = parseInt(partesHora[1], 10);
    var segundos = parseInt(partesHora[2], 10);

    // Obter a data atual
    var dataAtual = new Date();

    // Definir a hora na data atual
    dataAtual.setHours(horas);
    dataAtual.setMinutes(minutos);
    dataAtual.setSeconds(segundos);

    return dataAtual;
}

// Função para ler o arquivo CSV
function handleFileSelect(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        var contents = e.target.result;
        lerCSV(contents);
    };
    reader.readAsText(file);
}

function lerCSV(csv) {
    var lines = csv.trim().split('\n');
    lines.shift(); // Remove o cabeçalho
    
    lines.forEach(function(line) {
        var columns = line.split(';');
        var dataAulaParts = columns[8].split('/');
        var dataAula = new Date(dataAulaParts[2], dataAulaParts[1] - 1, dataAulaParts[0]);
        var datahoraInicio = criarDataComStringDeHora(columns[6]);
        var datahoraFim = criarDataComStringDeHora(columns[7]);
        var semanaAno = getSemanaAno(dataAula);
        var semanaSemestre = getSemanaSemestre(dataAula);
        
        tabledata.push({
            curso: columns[0],
            uc: columns[1],
            turno: columns[2],
            turma: columns[3],
            inscritos: columns[4],
            dia: columns[5],
            horaInicio: datahoraInicio.toLocaleTimeString(),
            horaFim: datahoraFim.toLocaleTimeString(),
            data: dataAula.toLocaleDateString(), //retorna a data sob a forma de string 
            caracteristicas: columns[9],
            sala: columns[10],
            semanaAno: semanaAno,
            semanaSemestre: semanaSemestre
        });
        
        salasOcupadas.push({
			sala: columns[10], // Coluna que contém o nome ou identificador da sala
            data: dataAula.toLocaleDateString(), // Coluna que contém a data da ocupação
            horaInicio: datahoraInicio.toLocaleTimeString(), // Coluna que contém a hora de início da ocupação
            horaFim: datahoraFim.toLocaleTimeString() // Coluna que contém a hora de término da ocupação
		})
    });
    // Inicializa a tabela Tabulator com os dados lidos
    iniciarTabela();
}

// Função para inicializar a tabela Tabulator
function iniciarTabela() {
    table = new Tabulator("#example-table", {
        data: tabledata,
        layout: "fitDataFill",
        pagination: "local",
        paginationSize: 10,
        paginationSizeSelector: [5, 10, 20, 40],
        movableColumns: true,
       // paginationCounter: "rows",
        initialSort: [{ column: "curso", dir: "asc" }],
        columns: [
            { title: "Curso", field: "curso", headerFilter: "input" },
            { title: "Unidade Curricular", field: "uc", headerFilter: "input" },
            { title: "Turno", field: "turno", headerFilter: "input" },
            { title: "Turma", field: "turma", headerFilter: "input" },
            { title: "Inscritos no turno", field: "inscritos", headerFilter: "input" },
            { title: "Dia da Semana", field: "dia", headerFilter: "input" },
            { title: "Hora início da aula", field: "horaInicio", headerFilter: "input" },
            { title: "Hora fim da aula", field: "horaFim", headerFilter: "input" },
            { title: "Data da aula", field: "data", headerFilter: "input", sorter: "date"},
            { title: "Características da sala pedida para a aula", field: "caracteristicas", headerFilter: "input" },
            { title: "Sala atribuída", field: "sala", headerFilter: "input" },
            { title: "Semana do ano", field: "semanaAno", headerFilter: "input" },
            { title: "Semana do semestre", field: "semanaSemestre", headerFilter: "input" },
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

// Função para calcular o número da semana do ano
function getSemanaAno(date) {   	
    var firstDayYear = new Date(date.getFullYear(), 0, 1); // Criar objeto Date para o primeiro dia do ano
    var diff = date.getTime() - firstDayYear.getTime(); // Calcular a diferença em milissegundos entre as duas datas    
    var oneWeek = 7 * 24 * 60 * 60 * 1000; // Definir a constante para uma semana em milissegundos
    var semanaAno = Math.floor(diff / oneWeek) + 1; // Calcular o número da semana do ano        
    return semanaAno;
}
	 
// Função para calcular a semana do semestre
function getSemanaSemestre(date) {
    var month = date.getMonth(); // Janeiro - 0, ...
    var firstDaySemester;
    
    if (month >= 8) { // De setembro a dezembro pertence ao 1º semestre
        firstDaySemester = new Date(date.getFullYear(), 8, 1); // 1 de Setembro - Data do início do 1º semestre
    } else if (month < 1) { // Janeiro pertence ao 1º semestre do ano anterior
        firstDaySemester = new Date(date.getFullYear() - 1, 8, 1); // 1 de Setembro - Data do início do 1º semestre do ano anterior
    } else { // De fevereiro a agosto pertence ao 2º semestre
        firstDaySemester = new Date(date.getFullYear(), 1, 1); // 1 de Fevereiro - Data do início do 2º semestre
    }
    
    var diff = date.getTime() - firstDaySemester.getTime();
    var oneWeek = 7 * 24 * 60 * 60 * 1000;
    var semanaSemestre = Math.floor(diff / oneWeek) + 1;
    return semanaSemestre;
}

function verSalasIscte(){
	window.location.href = "salas.html";
}



// Função para ler o arquivo CSV de salas existentes
function lerCSVSalasExistentes(csvSalasExistentes) {
    fetch(csvSalasExistentes)
        .then(response => response.text())
        .then(text => {
            var linhas = text.trim().split('\n');
            linhas.shift(); // Remove o cabeçalho
            
            linhas.forEach(function(line) {
                var columns = line.split(';');
                
                salasExistentes.push({
                    sala: columns[1],                   
                });
            });
        })
        .catch(error => console.error(error));
}

// Função para verificar se uma sala está disponível em um determinado horário
function salaEstaDisponivel(sala, data, hora) {
    
    // Verificar se a sala não está ocupada no intervalo de tempo especificado
    for (var i = 0; i < salasOcupadas.length; i++) {
        var ocupacao = salasOcupadas[i];
        
        if (ocupacao.sala == sala && ocupacao.data == data) {			
			if(ocupacao.horaInicio <= hora || ocupacao.horaFim >= hora){
				return false;
			}		
        }
    }
    return true; // A sala está disponível neste intervalo de tempo
}


// Função para verificar a disponibilidade das salas com base na data e hora selecionada
function verificarSalasDisponiveis() {
    var inputData = document.getElementById('Data').value;
    var inputHora = document.getElementById('Hora').value;
    
    if (!inputData || !inputHora) {
        alert('Por favor, selecione uma data e hora.');
        return;
    }   

    // Filtrar e exibir salas disponíveis com base na data e hora selecionada
    var salasDisponiveis = salasExistentes.filter(function(sala) {
        return salaEstaDisponivel(sala.sala, inputData, inputHora); // Verifique se a sala está disponível no horário selecionado
    }).map(function(sala) {
        return sala.sala;
    });

    if (salasDisponiveis.length === 0) {
        document.getElementById('salasDisponiveis').innerHTML = '<p>Nenhuma sala disponível para o horário selecionado.</p>';
    } else {
        document.getElementById('salasDisponiveis').innerHTML = '<p>Salas Disponíveis:</p><ul><li>' + salasDisponiveis.join('</li><li>') + '</li></ul>';
    }
}


lerCSVSalasExistentes('CaracterizacaoDasSalas.csv');








