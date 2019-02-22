from enum import Enum

def calcPosts(parcel):
	numPosts = 0
	gradient = Enum('down', 'up')
	prevGradient = None
	currGradient = None

	for k in range(1, len(parcel)):
		# Put post on mark = 0 and set first gradient
		if parcel[k - 1] < parcel[k]:
			currGradient = 'up'
		elif parcel[k - 1] > parcel[k]:
			currGradient = 'down'

		# Set prevGradient for the first slope encountered
		if prevGradient == None:
			prevGradient = currGradient

		if currGradient != prevGradient:
			numPosts += 1
			prevGradient = None

	return numPosts


if __name__ == "__main__":
	filename = "../testcase1.txt"
	with open(filename) as f:
		data = f.readlines()

	for i in range(2, len(data), 2):
		print(i)
		caseNum = i / 2

		parcel = data[i].split(' ')
		parcel = list(map(int, parcel))
		numPosts = calcPosts(parcel)

		print("case#{}: {}".format(caseNum, numPosts))

