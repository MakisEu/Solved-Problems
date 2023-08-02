class Solution:
    def minCostClimbingStairs(self, cost):
        #Recursive relation: Opt(n)=min(Opt(n-1),Opt(n-2))+cost[n]
        #Base case: F(0)=cost[0] F(1)=cost[1]
        cost.append(0)
        n=len(cost)
        F=[0 for _ in range(n+1)]
        F[0]=cost[0]
        F[1]=cost[1]
        for i in range(2,n):
            F[i]=min(F[i-1],F[i-2])
            F[i]+=cost[i]
        return F[n-1]

