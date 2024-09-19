import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        Professor prof1 = new Professor("Prof. João");
        Professor prof2 = new Professor("Prof. Maria");

        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        prof1.adicionarEscola(escola1);
        prof1.adicionarEscola(escola2);
        prof2.adicionarEscola(escola1);

        System.out.println("Professores na " + escola1.getNome() + ": " + escola1.professores);
        System.out.println("Professores na " + escola2.getNome() + ": " + escola2.professores);
        System.out.println("Escolas do " + prof1.getNome() + ": " + prof1.escolas);
        System.out.println("Escolas do " + prof2.getNome() + ": " + prof2.escolas);
    }

    static class Professor {
        private String nome;
        private Set<Escola> escolas;

        public Professor(String nome) {
            this.nome = nome;
            this.escolas = new HashSet<>();
        }

        public String getNome() {
            return nome;
        }

        public void adicionarEscola(Escola escola) {
            if (!escolas.contains(escola)) {
                escolas.add(escola);
                escola.adicionarProfessor(this);
            }
        }

        @Override
        public String toString() {
            return "Professor(" + nome + ")";
        }
    }

    static class Escola {
        private String nome;
        private Set<Professor> professores;

        public Escola(String nome) {
            this.nome = nome;
            this.professores = new HashSet<>();
        }

        public String getNome() {
            return nome;
        }

        public void adicionarProfessor(Professor professor) {
            if (!professores.contains(professor)) {
                professores.add(professor);
                professor.adicionarEscola(this);
            }
        }

        @Override
        public String toString() {
            return "Escola(" + nome + ")";
        }
    }
}
