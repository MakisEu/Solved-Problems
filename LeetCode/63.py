class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if (obstacleGrid[0][0]==1):
            return 0
        grid=[[0 for q in range(m)] for _ in range(n)]
        grid[0][0]=1
        for i in range(n):
            if (obstacleGrid[i][0]==1):
                break
            else:
                grid[i][0]=1
        for i in range(m):
            if (obstacleGrid[0][i]==1):
                break
            else:
                grid[0][i]=1
        for i in range(1,n):
            for j in range(1,m):
                if (obstacleGrid[i][j]==0):
                    grid[i][j]=grid[i-1][j]+grid[i][j-1]
                else:
                    grid[i][j]=0
        return grid[-1][-1]
