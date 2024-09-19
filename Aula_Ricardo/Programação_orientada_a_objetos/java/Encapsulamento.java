public class ContaBancaria {
    private String titular;
    private double saldo;

    public ContaBancaria(String titular) {
        this.titular = titular;
        this.saldo = 0.0;
    }

    public void depositar(double adicionar) {
        saldo += adicionar;
    }

    public void sacar(double remover) {
        saldo = Math.max(0, saldo - remover);
    }

    public void exibirSaldo() {
        System.out.println("Saldo: " + saldo);
    }

    public static void main(String[] args) {
        ContaBancaria titular1 = new ContaBancaria("etienne");
        titular1.depositar(100000);
        titular1.exibirSaldo();
    }
}
