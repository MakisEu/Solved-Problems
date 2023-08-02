class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt={}
        set1=set(s)
        for i in set1:
            dictt[i]=0
        for i in s:
            dictt[i]+=1
        if (set1!=set(t)):
            return False
        for i in t:
            dictt[i]-=1
        for i in dictt.values():
            if (i!=0):
                return False
        return True
