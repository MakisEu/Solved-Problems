class Solution:
    def climbStairs(self, n: int) -> int:
        waysPP=1
        waysP=1
        for i in range(2,n+1):
            waysP,waysPP=waysP+waysPP,waysP
        return waysP
