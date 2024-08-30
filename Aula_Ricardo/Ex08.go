//Maior e menor valor do array e sua média

package main

import (
	"fmt"
	"sort"
)

type vetorMedia struct {
	arr []int
}

func main() {
	v := vetorMedia{arr: []int{5, 7, 8, 12, 43, 21, 43, 12, 11, 99}}
	sort.Ints(v.arr)
	smallest := v.arr[0]
	largest := v.arr[len(v.arr)-1]
	average := float64(smallest+largest) / 2
	sum := int(smallest + largest)
	fmt.Printf("Smallest: %d\n", smallest)
	fmt.Printf("Largest: %d\n", largest)
	fmt.Printf("Sum: %d\n", sum)
	fmt.Printf("Average: %.2f\n", average)
}
