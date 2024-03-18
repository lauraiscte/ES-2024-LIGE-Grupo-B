package pt.iscte.gestaodehorarios;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Date;

import org.junit.jupiter.api.Test;

class LancaBrowserTest {

    @SuppressWarnings("deprecation")
	@Test
    public void testGetSemanaAno() {
        // Teste para a função getSemanaAno
        int semana1 = getSemanaAno(new Date(2023, 0, 2)); // Data: 1 de Janeiro de 2023
        int semana2 = getSemanaAno(new Date(2023, 0, 8)); // Data: 8 de Janeiro de 2023
        int semana3 = getSemanaAno(new Date(2023, 0, 15)); // Data: 15 de Janeiro de 2023
        assertEquals(1, semana1);
        assertEquals(2, semana2);
        assertEquals(3, semana3);
    }

    // Adicione um novo teste para testar a função getSemanaSemestre
    @SuppressWarnings("deprecation")
	@Test
    public void testGetSemanaSemestre() {
        // Teste para a função getSemanaSemestre
        int semana = getSemanaSemestre(new Date(2022, 8, 1)); // Data: 1 de Setembro de 2022
        int semana1Sem = getSemanaSemestre(new Date(2023, 0, 1)); // Data: 1 de Janeiro de 2023
        int semana2Sem = getSemanaSemestre(new Date(2023, 1, 1)); // Data: 1 de Fevereiro de 2023
        assertEquals(1, semana);
        assertEquals(18, semana1Sem);
        assertEquals(1, semana2Sem);
    }

    @SuppressWarnings("deprecation")
    private int getSemanaAno(Date date) {
        Date firstDayYear = new Date(date.getYear(), 0, 1);;

        long diff = date.getTime() - firstDayYear.getTime();
        long oneWeek = 7 * 24 * 60 * 60 * 1000L;
        int semanaAno = (int) Math.floor(diff / oneWeek) + 1;
        return semanaAno;
    }


    // Função para calcular a semana do semestre
    @SuppressWarnings("deprecation")
	private int getSemanaSemestre(Date date) {
        int month = date.getMonth(); // Janeiro - 0, ...
        Date firstDaySemester;
        
        if (month >= 8) { // De setembro a dezembro pertence ao 1º semestre
            firstDaySemester = new Date(date.getYear(), 8, 1); // 1 de Setembro - Data do início do 1º semestre
        } else if (month < 1) { // Janeiro pertence ao 1º semestre do ano anterior
            firstDaySemester = new Date(date.getYear() - 1, 8, 1); // 1 de Setembro - Data do início do 1º semestre do ano anterior
        } else { // De fevereiro a agosto pertence ao 2º semestre
            firstDaySemester = new Date(date.getYear(), 1, 1); // 1 de Fevereiro - Data do início do 2º semestre
        }
        
        long diff = date.getTime() - firstDaySemester.getTime();
        long oneWeek = 7 * 24 * 60 * 60 * 1000L;
        int semanaSemestre = (int) Math.floor(diff / oneWeek) + 1;
        return semanaSemestre;
    }

}
