def main():
  f = open("testcase1.txt")
  testCase = int(f.readline())

  while testCase > 0:
      K = int(f.readline())
      a = []
      line = f.readline()
      a = map(int, line.split(" "))
      maxPosts(a)
      testCase = testCase - 1

def maxPosts(arr):
    numPosts = -1
    gradient = 0
    newgrad = 0
    for i in (range(len(arr)-1)):
        if gradient == 0:
            if arr[i] < arr[i+1]:
                gradient = 1
            elif arr[i] > arr[i+1]:
                gradient = -1
            else:
                gradient = 0
        if gradient != 0:
            if arr[i] < arr[i+1]:
                newgrad = 1
            elif arr[i] > arr[i+1]:
                newgrad = -1
            else:
                newgrad = 0

            if (newgrad != gradient):
                numPosts = numPosts + 1
                gradient = 0 #reset
    print numPosts

if __name__ == "__main__":
    main()
