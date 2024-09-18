package main

import "fmt"

type ContaBancaria struct {
	Titular string
	Saldo   float64
}

func (c *ContaBancaria) Depositar(adicionar float64) {
	c.Saldo += adicionar
}

func (c *ContaBancaria) Sacar(remover float64) {
	if remover > c.Saldo {
		c.Saldo = 0
	} else {
		c.Saldo -= remover
	}
}

func (c *ContaBancaria) ExibirSaldo() {
	fmt.Printf("Saldo: %.2f\n", c.Saldo)
}

func main() {
	titular1 := ContaBancaria{Titular: "etienne"}

	titular1.Depositar(100000)
	titular1.ExibirSaldo()
}
