class SaldoInsuficiente extends Exception {
    public SaldoInsuficiente(String message) {
        super(message);
    }

    public SaldoInsuficiente() {
        super("Saldo insuficiente");
    }
}

public class ContaBancaria {
    private double saldo;

    public ContaBancaria(double saldo) {
        this.saldo = saldo;
    }

    public void depositar(double quantia) {
        saldo += quantia;
    }

    public void sacar(double quantia) throws SaldoInsuficiente {
        if (quantia > saldo) {
            throw new SaldoInsuficiente();
        }
        saldo -= quantia;
    }

    public double getSaldo() {
        return saldo;
    }

    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria(500);
        try {
            conta.sacar(499);
            System.out.println("Saque realizado com sucesso. Saldo atual: " + conta.getSaldo());
        } catch (SaldoInsuficiente e) {
            System.out.println(e.getMessage());
        }
    }
}
