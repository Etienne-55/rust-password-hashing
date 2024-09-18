package main

import "fmt"

type Animal interface {
	Som() string
}

type Cachorro struct{}

func (c Cachorro) Som() string {
	return "auau"
}

type Gato struct{}

func (g Gato) Som() string {
	return "miauu"
}

func main() {
	cachorro := Cachorro{}
	gato := Gato{}

	fmt.Printf("Cachorro: %s\n", cachorro.Som())
	fmt.Printf("Gato: %s\n", gato.Som())
}
