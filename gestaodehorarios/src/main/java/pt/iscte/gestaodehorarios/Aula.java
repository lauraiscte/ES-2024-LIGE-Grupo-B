package pt.iscte.gestaodehorarios;

public class Aula {
	private String curso;
	private String unidadeCurricular;
	private String turno;
	private String turma;
	private String numInscritosTurno;
	private String diaDaSemana;
	private String horaInicio;
	private String horaFim;
	private String data;
	private String caracteristicasSalaPedida;
	private String salaAtribuida;
	// Adicione outros atributos conforme necessário

	public Aula(String curso, String unidadeCurricular, String turno, String turma, String numInscritosTurno,
			String diaDaSemana, String horaInicio, String horaFim, String data, String caracteristicasSalaPedida,
			String salaAtribuida) {
		this.curso = curso;
		this.unidadeCurricular = unidadeCurricular;
		this.turno = turno;
		this.turma = turma;
		this.numInscritosTurno = numInscritosTurno;
		this.diaDaSemana = diaDaSemana;
		this.horaInicio = horaInicio;
		this.horaFim = horaFim;
		this.data = data;
		this.caracteristicasSalaPedida = caracteristicasSalaPedida;
		this.salaAtribuida = salaAtribuida;
	}

	public Aula () {
		// construtor sem argumentos??
	}
	
	
	@Override
	public String toString() {
		return "Aula [curso=" + curso + ", unidadeCurricular=" + unidadeCurricular + ", turno=" + turno + ", turma="
				+ turma + ", numInscritosTurno=" + numInscritosTurno + ", diaDaSemana=" + diaDaSemana + ", horaInicio="
				+ horaInicio + ", horaFim=" + horaFim + ", data=" + data + ", caracteristicasSalaPedida="
				+ caracteristicasSalaPedida + ", salaAtribuida=" + salaAtribuida + "]";
	}

	// Adicione getters e setters
	public String getCurso() {
		return curso;
	}

	public void setCurso(String curso) {
		this.curso = curso;
	}

	public String getUnidadeCurricular() {
		return unidadeCurricular;
	}

	public void setUnidadeCurricular(String unidadeCurricular) {
		this.unidadeCurricular = unidadeCurricular;
	}

	public String getTurno() {
		return turno;
	}

	public void setTurno(String turno) {
		this.turno = turno;
	}

	public String getTurma() {
		return turma;
	}

	public void setTurma(String turma) {
		this.turma = turma;
	}

	public String getNumInscritosTurno() {
		return numInscritosTurno;
	}

	public void setNumInscritosTurno(String numInscritosTurno) {
		this.numInscritosTurno = numInscritosTurno;
	}

	public String getDiaDaSemana() {
		return diaDaSemana;
	}

	public void setDiaDaSemana(String diaDaSemana) {
		this.diaDaSemana = diaDaSemana;
	}

	public String getHoraInicio() {
		return horaInicio;
	}

	public void setHoraInicio(String horaInicio) {
		this.horaInicio = horaInicio;
	}

	public String getHoraFim() {
		return horaFim;
	}

	public void setHoraFim(String horaFim) {
		this.horaFim = horaFim;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public String getCaracteristicasSalaPedida() {
		return caracteristicasSalaPedida;
	}

	public void setCaracteristicasSalaPedida(String caracteristicasSalaPedida) {
		this.caracteristicasSalaPedida = caracteristicasSalaPedida;
	}

	public String getSalaAtribuida() {
		return salaAtribuida;
	}

	public void setSalaAtribuida(String salaAtribuida) {
		this.salaAtribuida = salaAtribuida;
	}

}

