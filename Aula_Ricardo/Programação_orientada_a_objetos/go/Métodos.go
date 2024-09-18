package main

import "fmt"

type Carro struct {
	Marca      string
	Modelo     string
	Ano        int
	Velocidade int
}

func (c Carro) ExibirDetalhes() {
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func (c *Carro) Acelerar(incremento int) {
	c.Velocidade += incremento
}

func (c *Carro) Frear(decremento int) {
	if c.Velocidade-decremento < 0 {
		c.Velocidade = 0
	} else {
		c.Velocidade -= decremento
	}
}

func (c Carro) ExibirVelocidade() {
	fmt.Printf("A velocidade atual é de %d km/h\n", c.Velocidade)
}

func main() {
	carro1 := Carro{Marca: "Toyota", Modelo: "Land Cruiser", Ano: 2010}
	carro2 := Carro{Marca: "Honda", Modelo: "Civic", Ano: 2018}

	carro1.ExibirDetalhes()
	carro2.ExibirDetalhes()

	carro1.Acelerar(70)
	carro1.ExibirVelocidade()

	carro1.Frear(25)
	carro1.ExibirVelocidade()

	carro2.Acelerar(120)
	carro2.ExibirVelocidade()
}
