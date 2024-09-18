package main

import (
	"fmt"
)

type SaldoInsuficiente struct {
	Message string
}

func (e *SaldoInsuficiente) Error() string {
	return e.Message
}

type ContaBancaria struct {
	Saldo float64
}

func (c *ContaBancaria) Depositar(quantia float64) {
	c.Saldo += quantia
}

func (c *ContaBancaria) Sacar(quantia float64) error {
	if quantia > c.Saldo {
		return &SaldoInsuficiente{Message: "Saldo insuficiente"}
	}
	c.Saldo -= quantia
	return nil
}

func main() {
	conta := &ContaBancaria{Saldo: 500}

	err := conta.Sacar(499)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Saque realizado com sucesso!")
	}
}
