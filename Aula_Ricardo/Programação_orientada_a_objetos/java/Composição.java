class Motor {
    private String estado;

    public Motor() {
        this.estado = "desligado";
    }

    public String ligar() {
        this.estado = "ligado";
        return "Motor ligado";
    }

    public String desligar() {
        this.estado = "desligado";
        return "Motor desligado";
    }
}

class Carro {
    private Motor motor;

    public Carro() {
        this.motor = new Motor();
    }

    public String ligarCarro() {
        return motor.ligar();
    }

    public String desligarCarro() {
        return motor.desligar();
    }
}

public class Main {
    public static void main(String[] args) {
        Carro carro = new Carro();
        System.out.println(carro.ligarCarro());
        System.out.println(carro.desligarCarro());
    }
}
