package main

import (
	"fmt"
	"sync"
)

type Configuracao struct {
	Valor string
}

var instance *Configuracao
var once sync.Once

func GetInstance(valor string) *Configuracao {
	once.Do(func() {
		instance = &Configuracao{Valor: valor}
	})
	return instance
}

func main() {
	config1 := GetInstance("Configuração 1")
	fmt.Println(config1.Valor)

	config2 := GetInstance("Configuração 2")
	fmt.Println(config2.Valor)

	fmt.Println(config1 == config2)
}
