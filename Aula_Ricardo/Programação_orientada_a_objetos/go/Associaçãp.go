package main

import "fmt"

type Professor struct {
	Nome    string
	Escolas []*Escola
}

func (p *Professor) AdicionarEscola(escola *Escola) {
	for _, e := range p.Escolas {
		if e == escola {
			return
		}
	}
	p.Escolas = append(p.Escolas, escola)
	escola.AdicionarProfessor(p)
}

func (p Professor) String() string {
	return fmt.Sprintf("Professor(%s)", p.Nome)
}

type Escola struct {
	Nome        string
	Professores []*Professor
}

func (e *Escola) AdicionarProfessor(professor *Professor) {
	for _, p := range e.Professores {
		if p == professor {
			return
		}
	}
	e.Professores = append(e.Professores, professor)
	professor.AdicionarEscola(e)
}

func (e Escola) String() string {
	return fmt.Sprintf("Escola(%s)", e.Nome)
}

func main() {
	prof1 := &Professor{Nome: "Prof. João"}
	prof2 := &Professor{Nome: "Prof. Maria"}

	escola1 := &Escola{Nome: "Escola A"}
	escola2 := &Escola{Nome: "Escola B"}

	prof1.AdicionarEscola(escola1)
	prof1.AdicionarEscola(escola2)
	prof2.AdicionarEscola(escola1)

	fmt.Println("Professores na", escola1.Nome, escola1.Professores)
	fmt.Println("Professores na", escola2.Nome, escola2.Professores)

	fmt.Println("Escolas de", prof1.Nome, prof1.Escolas)
	fmt.Println("Escolas de", prof2.Nome, prof2.Escolas)
}
