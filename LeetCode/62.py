class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0 for q in range(m)] for _ in range(n)]
        grid[0][0]=1
        for i in range(1,m):
            grid[0][i]=1
        for j in range(1,n):
            grid[j][0]=1        
        #Recursive relation: F(i)(j)=F(i-1)(j)+F(i)(j-1)
        #F[i][j]=
        for j in range(1,m):
            for i in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]                
        return grid[-1][-1]

