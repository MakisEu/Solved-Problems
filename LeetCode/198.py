class Solution:
    def rob(self, nums):
        #Base case: F[0]=nums[0] F[1]=nums[1]
        n=len(nums)
        if (n<3):
            return max(nums)
        F=[0 for _ in range(n)]
        F[0]=nums[0]
        F[1]=max(nums[0],nums[1])
        #Recursive relation: F(n)=max(F(n-1),F(n-2)+nums[n])
        for i in range(2,n):
            F[i]=max(nums[i]+F[i-2],F[i-1])
        return F[-1]
