class Solution(object):

    def findCircleNum(self, M):
        def dfs(M, visited, col):
            for row in range(len(M)):
                # if there is a friendship and if friend has not already been added to circle
                if M[col][row] == 1 and visited[row] == 0:
                    visited[row] = 1
                    dfs(M, visited, row)
                # else it is no longer in the same circle of friends, so exit

        """
        :type M: List[List[int]] # adjacency matrix
        :rtype: int
        """
        visited = [0] * len(M) #create an array of zeros
        count = 0;
        for col in range(len(M)): #for every friend
            if (visited[col] == 0): #if not yet visited
                dfs(M, visited, col)
                count += 1
        return count

def stringToInt2dArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            M = stringToInt2dArray(line)
            
            ret = Solution().findCircleNum(M)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()