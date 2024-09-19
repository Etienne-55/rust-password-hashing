abstract class Animal {
    public abstract String som();
}

class Cachorro extends Animal {
    @Override
    public String som() {
        return "auau";
    }
}

class Gato extends Animal {
    @Override
    public String som() {
        return "miauu";
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();
        
        System.out.println("Cachorro: " + cachorro.som());
        System.out.println("Gato: " + gato.som());
    }
}
