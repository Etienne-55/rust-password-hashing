public class Produto {
    private String nome;
    private double valor;

    public Produto(String nome, double valor) {
        this.nome = nome;
        this.valor = valor;
    }

    public Produto add(Produto other) {
        if (other != null) {
            String novoNome = this.nome + " & " + other.nome;
            double novoValor = this.valor + other.valor;
            return new Produto(novoNome, novoValor);
        }
        return this; 
    }

    @Override
    public String toString() {
        return String.format("%s: R$%.2f", nome, valor);
    }

    public static void main(String[] args) {
        Produto produto1 = new Produto("Produto A", 22);
        Produto produto2 = new Produto("Produto B", 33);
        Produto produto3 = new Produto("Produto C", 65);

        Produto produto4 = produto1.add(produto2).add(produto3);

        System.out.println(produto4);
    }
}
