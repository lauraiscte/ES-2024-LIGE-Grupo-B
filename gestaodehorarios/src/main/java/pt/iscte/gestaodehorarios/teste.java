package pt.iscte.gestaodehorarios;

import java.util.List;

public class teste {
    public static void main(String[] args) {
        leitorCSV csvReaderExample = new leitorCSV();
        List<Aula> aulas = csvReaderExample.lerHorario("src/main/java/pt/iscte/gestaodehorarios/HorarioDeExemplo.csv");
        for (Aula aula : aulas) {
            System.out.println(aula); // Faça a saída dos dados como desejar
        }
    }
}
