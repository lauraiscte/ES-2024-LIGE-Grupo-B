var table;
var salasOcupadas = []; // Armazenará os dados das salas ocupadas
var salasExistentes = []; // Armazenará os dados das salas existentes
var salasDisponiveis = [];

// Função para inicializar a tabela Tabulator
function iniciarTabelaHorario(dados_para_tabela) {
    table = new Tabulator("#example-table", {
        data: dados_para_tabela,
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

function salaEstaDisponivel1(sala, data) {
    // Verificar se a sala não está ocupada no intervalo de tempo especificado
    for (var i = 0; i < salasOcupadas.length; i++) {
        var ocupacao = salasOcupadas[i];

        // Verificar se a sala está ocupada neste intervalo de tempo
	    if(ocupacao.data === data){
			console.log("o problema não é a data");
			if (ocupacao.sala === sala) {
	            return false; // A sala está ocupada neste intervalo de tempo
	        }
		}
    }
    return true; // A sala está disponível neste intervalo de tempo
}








