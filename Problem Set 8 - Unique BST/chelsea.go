package main

import (
	"fmt"
	"math"
)

var (
	unique int
)

func main() {
	fmt.Println(numTrees(4))
}

func numTrees(n int) int {
	unique = 0
	traverse(n, 0, []int{0})
	return unique
}

// Each time we look at all possible spots to put the next node and pick one
func traverse(n int, curr int, possibleSpots []int) {
	if curr == n {
		unique++
		return
	}

	// Pick a spot, branch off a new traverse with a node at that spot and updates new possible spots
	for ind, spot := range possibleSpots {
		fmt.Printf("put %d in %d, possible: %v\n", curr, spot, possibleSpots)
		possibleCopy := make([]int, len(possibleSpots)-1-ind)
		copy(possibleCopy, possibleSpots[ind+1:])

		// Remove curr spot and add new neighbours that opened up as possible spots
		children := getChildren(n, spot)
		possibleCopy = append(possibleCopy, children...)
		traverse(n, curr+1, possibleCopy)
	}
}

func getChildren(n int, node int) []int {
	numLeaves := int(math.Pow(2, float64(n-1)))
	if node >= numLeaves-1 {
		return []int{} // node is leaf node, no children
	}
	return []int{node*2 + 1, node*2 + 2}
}
