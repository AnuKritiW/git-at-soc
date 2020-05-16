package main

import (
	"fmt"
)

var (
	usedCombi map[int][]string //stores the words used to match the string so far
	// key:index of the string that has been matched so far
	// value: []combinations (eg. "cats and dog")
)

func main() {
	s := "catsanddog"
	wordDict := []string{"cat", "cats", "and", "sand", "dog"}
	result := wordBreak(s, wordDict)
	fmt.Printf("%v", result)
}

func wordBreak(s string, wordDict []string) []string {
	// Just storing the words in this map for easy retrieval
	wordMap := make(map[string]bool)
	for _, word := range wordDict {
		wordMap[word] = true
	}

	// Traverse and build all possible words combinations
	usedCombi = make(map[int][]string)
	traverseWord(s, 0, 1, wordMap)

	return usedCombi[len(s)]
}

// Start traversing the string by keeping 2 pointers and increasing the 2nd one.
// If the word fragment between the pointers matches a word, branch off a traversal that continues
// matching the rest of the string. The original traversal continues with increasing the 2nd one so
// that we get a longer fragment.
func traverseWord(s string, from int, to int, words map[string]bool) {
	if from >= len(s) {
		// found a match for all fragments in the word
		return
	}
	if to >= len(s)+1 {
		// finished traversing word
		return
	}

	fragment := s[from:to]
	matchedFragment := false
	if _, ok := words[fragment]; ok {
		// fragment matched a word given, append to previous used combinations
		matchedFragment = true
		if _, ok := usedCombi[to]; !ok {
			usedCombi[to] = make([]string, 0)
		}
		if from == 0 {
			// Start a new combi
			usedCombi[to] = append(usedCombi[to], fragment)
		} else {
			// Append to previous combis
			for _, prevCombi := range usedCombi[from] {
				if !exist(usedCombi[to], prevCombi+" "+fragment) {
					usedCombi[to] = append(usedCombi[to], prevCombi+" "+fragment)
				}
			}
		}
	}

	traverseWord(s, from, to+1, words)
	if matchedFragment {
		// fragment matched a word given, branch off a traversal that traverses the rest of the word
		traverseWord(s, to, to+1, words)
	}
}

func copySlice(slice []string) []string {
	copy := make([]string, len(slice))
	for ind, elem := range slice {
		copy[ind] = elem
	}
	return copy
}

func exist(slice []string, s string) bool {
	for _, elem := range slice {
		if elem == s {
			return true
		}
	}
	return false
}
