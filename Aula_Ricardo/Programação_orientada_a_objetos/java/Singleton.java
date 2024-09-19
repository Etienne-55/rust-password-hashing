public class Configuracao {
    private static Configuracao instance;
    
    private String valor;

    private Configuracao(String valor) {
        this.valor = valor;
    }

    public static Configuracao getInstance(String valor) {
        if (instance == null) {
            instance = new Configuracao(valor);
        }
        return instance;
    }

    public String getValor() {
        return valor;
    }

    public static void main(String[] args) {
        Configuracao config1 = Configuracao.getInstance("Configuração 1");
        System.out.println(config1.getValor());

        Configuracao config2 = Configuracao.getInstance("Configuração 2");
        System.out.println(config2.getValor());

        System.out.println(config1 == config2);
    }
}
