package main

import "fmt"

type Carro struct {
	Marca  string
	Modelo string
	Ano    int
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func main() {
	carro1 := Carro{Marca: "Toyota ", Modelo: "Land cruiser ", Ano: 2010}
	carro1.ExibirDetalhes()
}
