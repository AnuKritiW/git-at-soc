class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        lst = [0] * (n+1) #create a list of 0s of length 'n+1'
        lst[0:3] = [0, 1, 2]
        
        for i in range(3, n+1):
            for j in range(2, i):
                lst[i] += lst[j-1]*lst[i-j]
                
            lst[i] += lst[i-1]*2
        
        return lst[n]

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);
            
            ret = Solution().numTrees(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()