class Solution:
    def maxProfit(self, prices):
        maxProfit=0
        local_min=prices[0]
        for i in prices:
            maxProfit=max(maxProfit,i-local_min)
            local_min=min(local_min,i)
        return maxProfit

