package pt.iscte.gestaodehorarios;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.exceptions.CsvValidationException;

public class leitorCSV {

    public List<Aula> lerHorario(String caminhoArquivo) {
        List<Aula> aulas = new ArrayList<>();
        
        try (FileReader filereader = new FileReader(caminhoArquivo)) {
        	
        	CSVParser parser = new CSVParserBuilder().withSeparator(';').build(); 
        	CSVReader reader = new CSVReaderBuilder(filereader).withCSVParser(parser).build();
        	
        	String[] linha;
            reader.skip(1); // Pular a primeira linha (cabeçalho)
            while ((linha = reader.readNext()) != null) {
                Aula aula = new Aula();
                aula.setCurso(linha[0]);
                aula.setUnidadeCurricular(linha[1]);
                aula.setTurno(linha[2]);
                aula.setTurma(linha[3]);
                aula.setNumInscritosTurno(linha[4]);
                aula.setDiaDaSemana(linha[5]);
                aula.setHoraInicio(linha[6]);
                aula.setHoraFim(linha[7]);
                aula.setData(linha[8]);
                aula.setCaracteristicasSalaPedida(linha[9]);
                aula.setSalaAtribuida(linha[10]);
                
                aulas.add(aula);
            }
        } catch (IOException | CsvValidationException e) {
            e.printStackTrace();
        }
        return aulas;
    }
}