package main

import "fmt"

type Motor struct {
	HP   int
	Type string
}

type Car struct {
	Brand string
	Model string
	Motor Motor
}

func main() {
	motor := Motor{
		HP:   500,
		Type: "V8",
	}

	car := Car{
		Brand: "Ford",
		Model: "Mustang",
		Motor: motor,
	}

	fmt.Printf("Car: %s %s with Motor: %d HP %s\n", car.Brand, car.Model, car.Motor.HP, car.Motor.Type)
}
