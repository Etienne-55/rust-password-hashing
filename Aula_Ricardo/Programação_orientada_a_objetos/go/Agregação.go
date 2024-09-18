package main

import "fmt"

type Funcionario struct {
	Nome    string
	Cargo   string
	Salario float64
}

func (f Funcionario) String() string {
	return fmt.Sprintf("Funcionario Nome: %s, Cargo: %s, Salario: %.2f", f.Nome, f.Cargo, f.Salario)
}

type Empresa struct {
	Funcionarios []Funcionario
}

func (e *Empresa) AdicionarFuncionario(funcionario Funcionario) {
	e.Funcionarios = append(e.Funcionarios, funcionario)
}

func (e Empresa) ListarFuncionarios() {
	for _, funcionario := range e.Funcionarios {
		fmt.Println(funcionario)
	}
}

func main() {

	empresa := Empresa{}

	func1 := Funcionario{Nome: "Pedro", Cargo: "Vigia", Salario: 2000}

	empresa.AdicionarFuncionario(func1)

	empresa.ListarFuncionarios()
}
