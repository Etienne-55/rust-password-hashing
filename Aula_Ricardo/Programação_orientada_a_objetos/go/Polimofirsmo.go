package main

import "fmt"

type Animal interface {
	Som() string
}
type Vaca struct{}

func (v Vaca) Som() string {
	return "MUUU"
}

type Gato struct{}

func (g Gato) Som() string {
	return "Miau"
}

func EmitirSom(animais []Animal) {
	for _, animal := range animais {
		fmt.Println(animal.Som())
	}
}

func main() {

	animais := []Animal{Vaca{}, Gato{}}
	EmitirSom(animais)
}
