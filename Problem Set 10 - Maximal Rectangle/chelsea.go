package main

import "fmt"

func main() {
	input := [][]byte{
		[]byte("10100"),
		[]byte("10111"),
		[]byte("11111"),
		[]byte("10010"),
	}
	fmt.Printf("%d\n", maximalRectangle(input))
}

func maximalRectangle(matrix [][]byte) int {
	numRows := len(matrix)
	if numRows == 0 {
		return 0
	}
	numCols := len(matrix[0])

	maxRec := 0
	for origin := 0; origin < numRows; origin++ {
		heights := make([]int, numCols)
		for col, cell := range matrix[origin] {
			if cell == '1' {
				r := origin
				for r > 0 && matrix[r-1][col] == '1' {
					r--
				}
				heights[col] = origin - r + 1
			}
		}
		maxRec = max(largestRectangleArea(heights), maxRec) //maximum rectangle in histogram
	}

	return maxRec
}

func largestRectangleArea(heights []int) int {
	numBars := len(heights)

	// Make a map of where each height is located
	maxHeight := 0
	heightLocations := make(map[int][]int)
	for ind, ht := range heights {
		if _, ok := heightLocations[ht]; !ok {
			heightLocations[ht] = make([]int, 0)
		}
		heightLocations[ht] = append(heightLocations[ht], ind)

		maxHeight = max(maxHeight, ht)
	}

	// Start from calculating rectangles of height 1, 2, 3, etc...
	largest := 0
	for ht, inds := range heightLocations {
		leftBound := -1
		rightBound := -1
		for _, ind := range inds {
			if leftBound <= ind && rightBound >= ind {
				continue
			}
			leftBound = ind
			rightBound = ind
			// go left until we find left bound
			for leftBound > 0 && heights[leftBound-1] >= ht {
				leftBound--
			}
			for rightBound < numBars-1 && heights[rightBound+1] >= ht {
				rightBound++
			}
			rectangle := ht * (rightBound - leftBound + 1)
			largest = max(largest, rectangle)
		}
	}

	return largest
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
