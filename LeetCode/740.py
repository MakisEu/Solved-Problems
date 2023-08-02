class Solution:
    def deleteAndEarn(self, nums):
        #Create sums and sorted set
        if (len(nums)==0):
            return 0
        map={}
        for i in nums:
            try:
                map[i]+=i
            except:
                map[i]=i
        values=sorted(map.keys())
        n=len(values)
        #recursive relation: 
        #if *coflict extst :F(n)=max(F(n-1),F(n-2)+map(n)) 
        #else F(n)=F(n-1)+map(n)
        #*conflict: there exists a value that will get deleted by adding nums[i]
        
        #Edge cases
        if (n==1):
            return map[values[0]]
        if (n==2):
            if (abs(values[0]-values[1])==1):
                return max(map[values[0]],map[values[1]])
            else:
                return map[values[0]]+map[values[1]]
        #Base cases: F[0]=map[0] F[1]=recursive relation with F(n-2)=0
        F=[0 for _ in range(n+1)]
        F[0]=map[values[0]]
        if (abs(values[0]-values[1])==1):
            F[1]=max(F[0],map[values[1]])
        else:
            F[1]=F[0]+map[values[1]]
        for i in range(2,n):
            val=values[i]
            if (abs(val-values[i-1])==1):
                F[i]=max(F[i-1],F[i-2]+map[val])
            else:
                F[i]=F[i-1]+map[val]
        return F[n-1]
