package main

import "fmt"

type Imprimivel interface {
	Imprimir()
}

type Relatorio struct{}

func (r Relatorio) Imprimir() {
	fmt.Println("Imprimindo relatorio.")
}

type Contrato struct{}

func (c Contrato) Imprimir() {
	fmt.Println("Imprimindo contrato.")
}

func ProcessarImpressao(documento Imprimivel) {
	documento.Imprimir()
}

func main() {
	relatorio := Relatorio{}
	contrato := Contrato{}

	ProcessarImpressao(relatorio)
	ProcessarImpressao(contrato)
}
