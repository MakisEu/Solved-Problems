class Solution:
    def minPathSum(self, grid):
        #Recursive relation:F(n)(n)=min(F(n)(n-1),F(n-1)(n))+grid[n][n]
        F=[[0 for q in range(len(grid[0]))] for _ in range(len(grid))]
        F[0][0]=grid[0][0]
        for i in range(1,len(grid)):
            F[i][0]=grid[i][0]+F[i-1][0]
        for j in range(1,len(grid[0])):
            F[0][j]=grid[0][j]+F[0][j-1]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                F[i][j]=min(F[i][j-1],F[i-1][j])+grid[i][j]
        return F[-1][-1]
