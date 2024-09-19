abstract class Animal {
    abstract String som();
}

class Vaca extends Animal {
    @Override
    String som() {
        return "Muu";
    }
}

class Gato extends Animal {
    @Override
    String som() {
        return "Miau";
    }
}

public class Main {
    public static void emitirSom(Animal[] animais) {
        for (Animal animal : animais) {
            System.out.println(animal.som());
        }
    }

    public static void main(String[] args) {
        Animal[] animais = {new Vaca(), new Gato()};

        emitirSom(animais);
    }
}
