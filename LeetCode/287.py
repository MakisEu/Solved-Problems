def findDuplicate(nums):
        n=len(nums)
        l=0
        r=n-1
        flag=False
        while (l<r):
            if (nums[l]==nums[r]):
                return nums[l]
            if (flag):
                l+=1
                flag=False
            else:
                r-=1
                flag=True
        return 0
nums=[1,3,4,2,2]
print(findDuplicate(nums))
