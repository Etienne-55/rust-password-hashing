interface Imprimivel {
    void imprimir();
}

class Relatorio implements Imprimivel {
    @Override
    public void imprimir() {
        System.out.println("Imprimindo relatorio.");
    }
}

class Contrato implements Imprimivel {
    @Override
    public void imprimir() {
        System.out.println("Imprimindo contrato.");
    }
}

public class Main {
    public static void processarImpressao(Imprimivel documento) {
        documento.imprimir();
    }

    public static void main(String[] args) {
        Imprimivel relatorio = new Relatorio();
        Imprimivel contrato = new Contrato();

        processarImpressao(relatorio);
        processarImpressao(contrato);
    }
}
