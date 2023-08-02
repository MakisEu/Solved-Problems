class Solution:
    def maximumWealth(self, accounts):
        m=0
        for i in range(len(accounts)):
            m=max(sum(accounts[i]),m)
        return m
            
