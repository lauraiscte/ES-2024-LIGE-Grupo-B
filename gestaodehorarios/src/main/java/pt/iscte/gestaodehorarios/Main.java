package pt.iscte.gestaodehorarios;

import java.awt.Desktop;
//import java.awt.event.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
//import javax.swing.*;

public class Main {

    public static void main(String[] args) {

        // Definir o caminho do arquivo HTML que será gerado
        String htmlFilePath = "src/main/java/pt/iscte/gestaodehorarios/arquivo.html";

        // Ler os dados do CSV e gerar o HTML
        gerarHTML(htmlFilePath);

        // Lançar o navegador web para exibir o HTML gerado
        exibirHTML(htmlFilePath);
    }

    public static void gerarHTML(String filePath) {
        leitorCSV leitor = new leitorCSV();
        List<Aula> aulas = leitor.lerHorario("src/main/java/pt/iscte/gestaodehorarios/HorarioDeExemplo.csv");

        StringBuilder jsonData = new StringBuilder("[");
        for (Aula aula : aulas) {
            jsonData.append("{");
            jsonData.append("\"curso\": \"" + aula.getCurso() + "\",");
            jsonData.append("\"unidadeCurricular\": \"" + aula.getUnidadeCurricular() + "\",");
            jsonData.append("\"turno\": \"" + aula.getTurno() + "\",");
            jsonData.append("\"turma\": \"" + aula.getTurma() + "\",");
            jsonData.append("\"numInscritosTurno\": \"" + aula.getNumInscritosTurno() + "\",");
            jsonData.append("\"diaDaSemana\": \"" + aula.getDiaDaSemana() + "\",");
            jsonData.append("\"horaInicio\": \"" + aula.getHoraInicio() + "\",");
            jsonData.append("\"horaFim\": \"" + aula.getHoraFim() + "\",");
            jsonData.append("\"data\": \"" + aula.getData() + "\",");
            jsonData.append("\"caracteristicasSalaPedida\": \"" + aula.getCaracteristicasSalaPedida() + "\",");
            jsonData.append("\"salaAtribuida\": \"" + aula.getSalaAtribuida() + "\"");
            jsonData.append("},");
        }
        jsonData.deleteCharAt(jsonData.length() - 1);
        jsonData.append("]");

        // Escrever os dados no arquivo HTML
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("src/main/java/pt/iscte/gestaodehorarios/arquivo.html"))) {
            writer.write("<html lang=\"en\" xmlns=\"http://www.w3.org/1999/xhtml\">");
            writer.newLine();
            writer.write("<head>");
            writer.newLine();
            writer.write("<meta charset=\"utf-8\" />");
            writer.newLine();
            writer.write("<link href=\"https://unpkg.com/tabulator-tables@4.8.4/dist/css/tabulator.min.css\" rel=\"stylesheet\">");
            writer.newLine();
            writer.write("<script type=\"text/javascript\" src=\"https://unpkg.com/tabulator-tables@4.8.4/dist/js/tabulator.min.js\"></script>");
            writer.newLine();
            writer.write("</head>");
            writer.newLine();
            writer.write("<body>");
            writer.newLine();
            writer.write("<H1>Tipos de Salas de Aula</H1>");
            writer.newLine();
            writer.write("<div id=\"example-table\"></div>");
            writer.newLine();
            writer.write("<script type=\"text/javascript\">");
            writer.newLine();
            writer.write("var csvData = " + jsonData.toString() + ";");
            writer.newLine();
            writer.write("var table = new Tabulator(\"#example-table\", {");
            writer.newLine();
            writer.write("data: csvData,");
            writer.newLine();
            writer.write("layout:\"fitDatafill\",");
            writer.newLine();
            writer.write("pagination:\"local\",");
            writer.newLine();
            writer.write("paginationSize:10,");
            writer.newLine();
            writer.write("paginationSizeSelector:[5, 10, 20, 40],");
            writer.newLine();
            writer.write("movableColumns:true,");
            writer.newLine();
            writer.write("paginationCounter:\"rows\",");
            writer.newLine();
            writer.write("initialSort:[{column:\"building\",dir:\"asc\"}],");
            writer.newLine();
            writer.write("columns:[");
            writer.newLine();
            writer.write("{title:\"Descrição do Tipo de Sala\", field:\"classroomtypedescription\", headerFilter:\"input\"},");
            writer.newLine();
            writer.write("{title:\"Quantidade\", field:\"amountofclassroomsofthistype\", headerFilter:\"input\"},");
            writer.newLine();
            writer.write("{title:\"Sala\", field:\"classroomsids\", headerFilter:\"input\"},");
            writer.newLine();
            writer.write("],");
            writer.newLine();
            writer.write("});");
            writer.newLine();
            writer.write("</script>");
            writer.newLine();
            writer.write("</body>");
            writer.newLine();
            writer.write("</html>");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void exibirHTML(String filePath) {
        try {
            Desktop desk = Desktop.getDesktop();
            desk.browse(new File(filePath).toURI());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
