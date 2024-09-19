abstract class Funcionario {
    public abstract double calcularSalario();
}

class FuncionarioHorista extends Funcionario {
    private double valorHora;
    private double horasTrabalhadas;

    public FuncionarioHorista(double valorHora, double horasTrabalhadas) {
        this.valorHora = valorHora;
        this.horasTrabalhadas = horasTrabalhadas;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorHora;
    }
}

class FuncionarioAssalariado extends Funcionario {
    private double salarioMensal;

    public FuncionarioAssalariado(double salarioMensal) {
        this.salarioMensal = salarioMensal;
    }

    @Override
    public double calcularSalario() {
        return salarioMensal;
    }
}

public class Main {
    public static void main(String[] args) {
        FuncionarioHorista horista = new FuncionarioHorista(100, 20);
        FuncionarioAssalariado assalariado = new FuncionarioAssalariado(2000);

        System.out.println("Salário do Horista: " + horista.calcularSalario());
        System.out.println("Salário do Assalariado: " + assalariado.calcularSalario());
    }
}
