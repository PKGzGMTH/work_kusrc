package main

import "fmt"

func main() {
	names := []string{"Harry", "Ron", "Hermione"}
	fmt.Println(names)
	for x := 0; x < len(names); x++ {
		fmt.Println(x, names[x])
	}

	for {
		fmt.Println("hi")
	}

}
