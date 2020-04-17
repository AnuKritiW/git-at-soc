def findCircleNum(self, M):
    if not M: 
        return 0
    
    def dfs(i):
        if i < 0 or i >= len(M) or M[i][i] == 0:
            return
        M[i][i] = 0
        for j, nbr in enumerate(M[i]):
            if nbr == 1:
                dfs(j)
        
    count = 0
    for i in range(len(M)):
        if M[i][i] == 1:
            count += 1
            dfs(i)
            
    return count
