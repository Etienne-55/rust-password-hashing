package main

import "fmt"

type Funcionario interface {
	CalcularSalario() float64
}

type FuncionarioHorista struct {
	ValorHora        float64
	HorasTrabalhadas float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return f.HorasTrabalhadas * f.ValorHora
}

type FuncionarioAssalariado struct {
	SalarioMensal float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.SalarioMensal
}

func main() {
	horista := FuncionarioHorista{ValorHora: 100, HorasTrabalhadas: 20}
	assalariado := FuncionarioAssalariado{SalarioMensal: 2000}

	fmt.Println(horista.CalcularSalario())
	fmt.Println(assalariado.CalcularSalario())
}
