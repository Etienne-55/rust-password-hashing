public class Calculadora {
    
    public int somar(int a, int b) {
        return a + b;
    }

    public int somar(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        System.out.println(calc.somar(1, 2)); 

        System.out.println(calc.somar(1, 2, 3)); 
    }
}
