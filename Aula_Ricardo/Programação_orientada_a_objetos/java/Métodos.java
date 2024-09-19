public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }

    public void exibirDetalhes() {
        System.out.println("Marca: " + marca + ", Modelo: " + modelo + ", Ano: " + ano);
    }

    public void acelerar(int incremento) {
        velocidade += incremento;
    }

    public void frear(int decremento) {
        velocidade = Math.max(0, velocidade - decremento);
    }

    public void exibirVelocidade() {
        System.out.println("A velocidade atual é de " + velocidade + " km/h");
    }

    public static void main(String[] args) {
        Carro carro1 = new Carro("Toyota", "Land cruiser", 2010);
        Carro carro2 = new Carro("Honda", "Civic", 2018);

        carro1.exibirDetalhes();
        carro2.exibirDetalhes();

        carro1.acelerar(70);
        carro1.exibirVelocidade();
        carro1.frear(25);
        carro1.exibirVelocidade();

        carro2.acelerar(120);
        carro2.exibirVelocidade();
    }
}
