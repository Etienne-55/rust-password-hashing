//Par e impar em go

package main

import "fmt"

func main() {

	var num1, num2 int

	fmt.Print("Enter the first number: ")
	fmt.Scan(&num1)
	fmt.Print("Enter the seconde number: ")
	fmt.Scan(&num2)

	result := num1 + num2

	if result%2 == 0 {
		fmt.Print(result, " is evem")
	} else {
		fmt.Println(result, "is odd")
	}

}
