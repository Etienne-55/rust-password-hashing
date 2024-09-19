import java.util.ArrayList;
import java.util.List;

class Funcionario {
    private String nome;
    private String cargo;
    private double salario;

    public Funcionario(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Funcionario Nome: " + nome + ", Cargo: " + cargo + ", Salario: " + salario;
    }
}

class Empresa {
    private List<Funcionario> funcionarios;

    public Empresa() {
        funcionarios = new ArrayList<>();
    }

    public void adicionarFuncionario(Funcionario funcionario) {
        funcionarios.add(funcionario);
    }

    public void listarFuncionarios() {
        for (Funcionario funcionario : funcionarios) {
            System.out.println(funcionario);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Empresa empresa = new Empresa();

        Funcionario func1 = new Funcionario("Pedro", "Vigia", 2000);

        empresa.adicionarFuncionario(func1);

        empresa.listarFuncionarios();
    }
}
