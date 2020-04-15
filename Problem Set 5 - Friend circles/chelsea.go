package main

// Time: 35.37 (not so good!)

// Friend circle of person with `id`. Points to a parent friend and contains a circle of `id`'s friends
type Circle struct {
	id      int
	parent  int // the parent friend is the lowest id in the circle
	friends map[int]bool
}

func NewCircle(me int) *Circle {
	friends := make(map[int]bool)
	friends[me] = true // friend circle only contains yourself at first
	return &Circle{
		id:      me,
		parent:  me,
		friends: friends,
	}
}

// --- end Circle

// Merge the 2 circles by pointing both to a common parent friend and updating all friend's circles
func merge(circles map[int]*Circle, personA int, personB int) {
	// fmt.Printf("%v and %v \n", s, beta)
	// The alpha should have lower id
	var alpha *Circle
	var beta *Circle
	if circles[personA].parent < circles[personB].parent {
		alpha = circles[personA]
		beta = circles[personB]
	} else {
		alpha = circles[personB]
		beta = circles[personA]
	}

	// Merge beta's friends into alpha's friends
	for key := range beta.friends {
		if _, ok := alpha.friends[key]; !ok {
			alpha.friends[key] = true
		}
	}
	// Track down all of alpha and beta's friends to update their circle
	for person := range alpha.friends {
		circles[person].friends = alpha.friends
	}
	for person := range beta.friends {
		circles[person].parent = alpha.parent
		circles[person].friends = alpha.friends
	}
}

func findCircleNum(M [][]int) int {
	//assume everyone is in their own friend circle and merge them
	circles := make(map[int]*Circle) //map of id : friend circle
	for i := 0; i < len(M); i++ {
		circles[i] = NewCircle(i)
	}

	for person, friends := range M {
		for otherPerson, val := range friends {
			if val == 1 && person != otherPerson {
				// friends!
				// Now check if they were merged before by checking if they have same parent
				if circles[person].parent != circles[otherPerson].parent {
					merge(circles, person, otherPerson)
				}
			}
		}
	}

	// Count unique parents
	unique := make(map[int]bool)
	for person := range circles {
		unique[circles[person].parent] = true
	}

	return len(unique)
}
