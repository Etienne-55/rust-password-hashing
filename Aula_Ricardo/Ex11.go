package main

import "fmt"

func main() {

	var lado_maior, lado_menor int

	fmt.Print("Valor área menor: ")
	fmt.Scan(&lado_menor)
	fmt.Print("Valor área maior: ")
	fmt.Scan(&lado_maior)

	area := int(lado_menor * lado_maior)
	perimetro := int(lado_menor*2 + lado_maior*2)

	println("Valor da área: ", area)
	println("Valor do perimetro: ", perimetro)
}
