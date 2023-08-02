class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map={}
        map2={}
        for i in magazine:
            try:
                map[i]+=1
            except:
                map[i]=1
        for i in ransomNote:
            try:
                map2[i]+=1
            except:
                map2[i]=1
        for i in map2.keys():
            try:
                if (map[i]<map2[i]):
                    return False
            except:
                return False
        return True

