package main

import "fmt"

type Calculadora struct{}

func (c Calculadora) Somar(a, b int, extra ...int) int {
	if len(extra) > 0 {
		return a + b + extra[0]
	}
	return a + b
}

func main() {
	calc := Calculadora{}

	fmt.Println(calc.Somar(1, 2))

	fmt.Println(calc.Somar(1, 2, 3))
}
