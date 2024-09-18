package main

import "fmt"

type Produto struct {
	Nome  string
	Valor float64
}

func (p Produto) Adicionar(other Produto) Produto {
	return Produto{
		Nome:  p.Nome + " & " + other.Nome,
		Valor: p.Valor + other.Valor,
	}
}

func (p Produto) String() string {
	return fmt.Sprintf("%s: R$%.2f", p.Nome, p.Valor)
}

func main() {
	produto1 := Produto{Nome: "Produto A", Valor: 22.0}
	produto2 := Produto{Nome: "Produto B", Valor: 33.0}
	produto3 := Produto{Nome: "Produto C", Valor: 65.0}

	produto4 := produto1.Adicionar(produto2).Adicionar(produto3)

	fmt.Println(produto4)
}
